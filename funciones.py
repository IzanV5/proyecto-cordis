"""Funciones compartidas por los tres cuadernos del proyecto CORDIS.

La preparación de etiquetas y las representaciones parten del cuaderno original.
Cada cuaderno se puede abrir por separado y usa las mismas particiones.
Responsable del mantenimiento de este archivo: Izan.
"""

import ast
import hashlib
from pathlib import Path

import numpy as np
import pandas as pd


RAIZ = Path(__file__).resolve().parent
DATOS = RAIZ / "datos"
CACHE = DATOS / "cache"
RESULTADOS = RAIZ / "resultados"
FIGURAS = RESULTADOS / "graficas"
PARTICIONES = RESULTADOS / "particiones.csv"
SEMILLA = 42
NOMBRES_CONJUNTOS = ("train", "val", "test")


def cargar_datos(carpeta=DATOS):
    """Lee los dos Excel desde la carpeta local indicada."""
    carpeta = Path(carpeta)
    rutas = [carpeta / "projects.xlsx", carpeta / "SciVocCodes.xlsx"]
    ausentes = [ruta.name for ruta in rutas if not ruta.is_file()]
    if ausentes:
        raise FileNotFoundError(
            f"Faltan {', '.join(ausentes)} en {carpeta}. "
            "Copia ahí los Excel proporcionados por el profesor."
        )
    return tuple(pd.read_excel(ruta) for ruta in rutas)


def convertir_codigos(valor):
    """Convierte las listas de códigos guardadas como texto en el Excel."""
    if isinstance(valor, (list, tuple)):
        return list(valor)
    if pd.isna(valor):
        return []
    if isinstance(valor, str):
        resultado = ast.literal_eval(valor)
        if isinstance(resultado, (list, tuple)):
            return list(resultado)
    raise ValueError(f"Lista EuroSciVoc con formato inesperado: {valor!r}")


def preparar_datos(projects, scivoc):
    """Asigna la primera etiqueta válida de nivel 2 y su raíz de nivel 1.

    Mantiene la regla del cuaderno original. Las fechas ausentes se conservan:
    si se usan en un modelo, la imputación debe ajustarse con entrenamiento.
    """
    catalogo = scivoc.dropna(subset=["code"]).copy()
    jerarquias = {
        int(fila.code): [int(x) for x in str(fila.full_code).split("/") if x]
        for fila in catalogo.itertuples()
    }
    nombres = dict(zip(catalogo["code"].astype(int), catalogo["title"]))

    df = projects.dropna(subset=["euroSciVocCode"]).copy()
    df["euroSciVocCode"] = df["euroSciVocCode"].map(convertir_codigos)

    def etiquetas(codigos):
        for codigo in codigos:
            niveles = jerarquias.get(int(codigo), [])
            if len(niveles) >= 2:
                return niveles[0], niveles[1]
        return np.nan, np.nan

    etiquetas_proyecto = df["euroSciVocCode"].map(etiquetas)
    df["label_nivel1"] = etiquetas_proyecto.map(lambda par: par[0])
    df["label_nivel2"] = etiquetas_proyecto.map(lambda par: par[1])
    df = df.dropna(subset=["label_nivel2"]).copy()
    df[["label_nivel1", "label_nivel2"]] = df[
        ["label_nivel1", "label_nivel2"]
    ].astype(int)
    df["categoria_nivel2"] = df["label_nivel2"].map(nombres)
    df["summary"] = df["summary"].fillna("").astype(str)

    for columna in ("startDate", "endDate"):
        df[columna] = pd.to_datetime(df[columna], errors="coerce")
    for columna in ("publicationID", "patentID"):
        df[columna] = df[columna].fillna("[]")

    if df["projectID"].duplicated().any():
        raise ValueError("Hay projectID repetidos; revisadlos antes de dividir los datos.")
    return df.reset_index(drop=True)


def indices_particiones(etiquetas, semilla=SEMILLA):
    """Devuelve índices estratificados: 60 % train, 30 % val y 10 % test."""
    from sklearn.model_selection import train_test_split

    etiquetas = np.asarray(etiquetas)
    indices = np.arange(len(etiquetas))
    train, temporal = train_test_split(
        indices, test_size=0.40, random_state=semilla, stratify=etiquetas
    )
    val, test = train_test_split(
        temporal,
        test_size=0.25,
        random_state=semilla,
        stratify=etiquetas[temporal],
    )
    return dict(zip(NOMBRES_CONJUNTOS, (train, val, test)))


def cargar_o_crear_particiones(df, ruta=PARTICIONES):
    """Reutiliza el reparto guardado y comprueba que IDs y etiquetas coinciden.

    El orden se guarda para que las matrices de los cuadernos correspondan
    siempre a los mismos proyectos. Si cambian las etiquetas, hay que revisar
    el reparto entre todos antes de sustituir el CSV.
    """
    ruta = Path(ruta)
    columnas = ["projectID", "label_nivel1", "label_nivel2"]
    if df.empty or df["projectID"].duplicated().any():
        raise ValueError("Se necesitan proyectos válidos con identificadores únicos.")

    if not ruta.exists():
        partes = []
        for nombre, indices in indices_particiones(df["label_nivel2"]).items():
            parte = df.iloc[indices][columnas].copy()
            parte["conjunto"] = nombre
            parte["orden"] = np.arange(len(parte))
            partes.append(parte)
        reparto = pd.concat(partes, ignore_index=True)
        ruta.parent.mkdir(parents=True, exist_ok=True)
        reparto.to_csv(ruta, index=False)
    else:
        reparto = pd.read_csv(ruta)

    requeridas = set(columnas + ["conjunto", "orden"])
    if not requeridas.issubset(reparto.columns):
        raise ValueError("El CSV de particiones no tiene las columnas necesarias.")
    if reparto["projectID"].duplicated().any():
        raise ValueError("Hay proyectos repetidos en las particiones guardadas.")
    if set(reparto["projectID"]) != set(df["projectID"]):
        raise ValueError("Han cambiado los proyectos. Revisad el CSV de particiones.")
    if set(reparto["conjunto"]) != set(NOMBRES_CONJUNTOS):
        raise ValueError("Las particiones deben contener train, val y test.")

    actual = df.set_index("projectID")
    guardado = reparto.set_index("projectID")
    for columna in ("label_nivel1", "label_nivel2"):
        if not np.array_equal(
            actual.loc[guardado.index, columna].to_numpy(),
            guardado[columna].to_numpy(),
        ):
            raise ValueError("Han cambiado las etiquetas. Revisad las particiones.")

    conjuntos = {}
    for nombre in NOMBRES_CONJUNTOS:
        parte = reparto[reparto["conjunto"] == nombre].sort_values("orden")
        if not np.array_equal(parte["orden"].to_numpy(), np.arange(len(parte))):
            raise ValueError(f"El orden de la partición {nombre} no es válido.")
        conjuntos[nombre] = actual.loc[parte["projectID"]].reset_index()
    return conjuntos


def preprocesar_resumenes(textos, nlp=None):
    """Lematiza, pasa a minúsculas y elimina stopwords y tokens cortos."""
    if nlp is None:
        import spacy

        try:
            nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])
        except OSError as error:
            raise OSError(
                "Falta el modelo de inglés. Ejecuta: "
                "python -m spacy download en_core_web_sm"
            ) from error
    return [
        " ".join(
            token.lemma_.lower()
            for token in doc
            if token.is_alpha and not token.is_stop and len(token.text) > 2
        )
        for doc in nlp.pipe(textos, batch_size=256)
    ]


def crear_tfidf(documentos, **parametros):
    """Aprende el vocabulario con train y transforma val y test."""
    from sklearn.feature_extraction.text import TfidfVectorizer

    opciones = dict(max_features=10000, min_df=5, max_df=0.90, ngram_range=(1, 2))
    opciones.update(parametros)
    modelo = TfidfVectorizer(**opciones)
    matrices = {"train": modelo.fit_transform(documentos["train"])}
    for nombre in ("val", "test"):
        matrices[nombre] = modelo.transform(documentos[nombre])
    return modelo, matrices


def obtener_embedding_documento(tokens, modelo):
    """Promedia palabras conocidas; usa ceros si no hay ninguna."""
    vectores = [modelo.wv[palabra] for palabra in tokens if palabra in modelo.wv]
    if not vectores:
        return np.zeros(modelo.vector_size, dtype=np.float32)
    return np.mean(vectores, axis=0).astype(np.float32)


def crear_word2vec(documentos, **parametros):
    """Entrena Word2Vec solo con train y calcula la media por documento."""
    from gensim.models import Word2Vec

    tokens = {nombre: [doc.split() for doc in docs] for nombre, docs in documentos.items()}
    opciones = dict(
        vector_size=300, window=5, min_count=2, workers=1, sg=1, epochs=10, seed=SEMILLA
    )
    opciones.update(parametros)
    modelo = Word2Vec(sentences=tokens["train"], **opciones)
    matrices = {
        nombre: np.vstack([obtener_embedding_documento(doc, modelo) for doc in docs])
        for nombre, docs in tokens.items()
    }
    resumen = []
    for nombre, docs in tokens.items():
        total = sum(len(doc) for doc in docs)
        desconocidas = sum(palabra not in modelo.wv for doc in docs for palabra in doc)
        vacios = sum(not any(palabra in modelo.wv for palabra in doc) for doc in docs)
        resumen.append(
            dict(
                conjunto=nombre,
                tokens=total,
                tokens_oov=desconocidas,
                porcentaje_oov=100 * desconocidas / total if total else 0,
                documentos_sin_vector=vacios,
            )
        )
    return modelo, matrices, pd.DataFrame(resumen)


def _huella(df):
    columnas = ["projectID", "summary", "label_nivel1", "label_nivel2"]
    contenido = df[columnas].to_csv(index=False, lineterminator="\n")
    return hashlib.sha256(contenido.encode("utf-8")).hexdigest()


def guardar_representacion(nombre, matrices, conjuntos):
    """Guarda vectores locales junto a la huella de los proyectos y su orden."""
    import joblib

    if set(matrices) != set(NOMBRES_CONJUNTOS):
        raise ValueError("Hay que guardar matrices de train, val y test.")
    for parte in NOMBRES_CONJUNTOS:
        if matrices[parte].shape[0] != len(conjuntos[parte]):
            raise ValueError(f"La matriz de {parte} no coincide con sus proyectos.")
    CACHE.mkdir(parents=True, exist_ok=True)
    ruta = CACHE / f"{nombre}.joblib"
    joblib.dump(
        dict(matrices=matrices, huellas={k: _huella(conjuntos[k]) for k in NOMBRES_CONJUNTOS}),
        ruta,
        compress=3,
    )
    return ruta


def cargar_representacion(nombre, conjuntos):
    """Carga vectores y detecta cambios de datos o del orden de los proyectos."""
    import joblib

    ruta = CACHE / f"{nombre}.joblib"
    if not ruta.exists():
        cuaderno = "03_bert_y_comparacion.ipynb" if nombre == "bert" else "01_datos_y_representaciones.ipynb"
        raise FileNotFoundError(f"Falta {ruta.name}. Genera los vectores en {cuaderno}.")
    contenido = joblib.load(ruta)
    for parte in NOMBRES_CONJUNTOS:
        if contenido["huellas"][parte] != _huella(conjuntos[parte]):
            raise ValueError(f"Los vectores {nombre} ya no corresponden a los datos. Genéralos de nuevo.")
        if contenido["matrices"][parte].shape[0] != len(conjuntos[parte]):
            raise ValueError(f"El número de vectores {nombre} de {parte} es incorrecto.")
    return contenido["matrices"]


def evaluar(y_real, y_predicha, clases=None):
    """Calcula las dos métricas principales con las mismas clases de referencia."""
    from sklearn.metrics import accuracy_score, f1_score

    return dict(
        accuracy=float(accuracy_score(y_real, y_predicha)),
        macro_f1=float(
            f1_score(y_real, y_predicha, labels=clases, average="macro", zero_division=0)
        ),
    )


def guardar_metricas(experimento, representacion, modelo, nivel, conjunto, metricas):
    """Añade o actualiza una fila de resultados de un experimento concreto."""
    RESULTADOS.mkdir(parents=True, exist_ok=True)
    ruta = RESULTADOS / "metricas.csv"
    fila = dict(
        experimento=experimento,
        representacion=representacion,
        modelo=modelo,
        nivel=nivel,
        conjunto=conjunto,
        **metricas,
    )
    if ruta.exists():
        tabla = pd.read_csv(ruta)
        misma = (
            (tabla["experimento"] == experimento)
            & (tabla["nivel"] == nivel)
            & (tabla["conjunto"] == conjunto)
        )
        tabla = tabla.loc[~misma]
        tabla = pd.concat([tabla, pd.DataFrame([fila])], ignore_index=True)
    else:
        tabla = pd.DataFrame([fila])
    tabla.to_csv(ruta, index=False)
    return tabla
