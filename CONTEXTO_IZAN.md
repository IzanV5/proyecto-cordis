# Contexto de Izan: proyecto CORDIS

Somos Mónica, Izan y Sara. Este documento sirve para continuar mi parte con
una IA que tenga acceso al repositorio. Hay que inspeccionar los archivos antes
de actuar y distinguir el código escrito de los resultados realmente ejecutados.

Repositorio: https://github.com/IzanV5/proyecto-cordis

## Reparto y alcance

- Mónica: `01_datos_y_representaciones.ipynb`, datos, etiquetas, exploración,
  TF-IDF y Word2Vec. También entregó `Version2_01_datos_y_representaciones.ipynb`.
- Izan: `02_modelos_y_extension.ipynb`, clásicos, red PyTorch, extensión,
  reproducibilidad y mantenimiento exclusivo de `funciones.py`.
- Sara: `03_bert_y_comparacion.ipynb`, BERT congelado, fine-tuning y comparación.
- README compartido. Se conserva el crédito del cuaderno original de Mónica.

Mantenerlo sencillo: tres cuadernos principales, funciones compartidas y README
como informe. No reescribir los cuadernos de mis compañeras ni crear una aplicación.
Solo Izan modifica `funciones.py`, manteniendo su compatibilidad.

El enunciado es `Proyecto_Final_CORDIS_ES_v2.pdf`, normalmente en la carpeta
superior al repositorio. `Reparto_y_calendario_CORDIS.pdf` es nuestro plan, no
el enunciado oficial. Consultar el README para el informe y las figuras.

## Estado comprobado el 18 de noviembre de 2026

Mi parte de código está ejecutada: seis regresiones logísticas (tres
representaciones por dos niveles), dos redes PyTorch con Word2Vec y dos
regresiones de la extensión en nivel 2 (metadatos y TF-IDF + metadatos).
La referencia de texto de la extensión reutiliza TF-IDF del experimento básico.

Las configuraciones se eligieron con validación el 10 de noviembre. El ZIP
posterior de Mónica contiene matrices idénticas a las utilizadas entonces.
Sara entregó la caché BERT; está en `datos/cache/bert.joblib`.
El 18 de noviembre se evaluaron los diez modelos en test sin volver a elegir
parámetros ni reentrenar clasificadores.

Hay 20 filas en `resultados/metricas_izan.csv`, predicciones de validación y test
de los diez modelos, informes por clase, curvas, confusiones, comparación de
representaciones, extensión, bootstrap pareado y errores. El cuaderno contiene
las salidas reales. `resultados/README.md` explica los archivos.

TF-IDF con LR obtiene macro-F1 0,3992 en nivel 2 y 0,6072 en nivel 1 en test.
No se deben usar estas cifras para modificar ahora las configuraciones.
El test del fine-tuning y la comparación conjunta de test corresponden a Sara.
Las diapositivas están aplazadas por petición expresa de Izan: centrarse en
código y resultados hasta que pida prepararlas.

## Datos y protocolo

Los Excel locales son `datos/projects.xlsx` y `datos/SciVocCodes.xlsx`.
35.378 proyectos iniciales, 31.982 válidos (90,40 %), 39 clases de nivel 2 y seis
de nivel 1. Se toma el primer código original que tenga un ancestro válido de
nivel 2 y su raíz. Mónica documentó la diferencia con el 90,31 % aproximado.

`resultados/particiones.csv` conserva 60/30/10, semilla 42 y estratificación
por nivel 2: train 19.189, val 9.594, test 3.199. No cambiarlo ni alterar las
etiquetas por separado. Las predicciones mantienen `projectID` y códigos
EuroSciVoc reales, no índices de la red.

Vectorizadores, Word2Vec, escalado, imputación y one-hot se ajustan solo con
train. Hiperparámetros y parada de la red se eligieron con validación.
La extensión usa logaritmos de coste y contribución UE, duración, número de
países y país coordinador, sin identificadores ni etiquetas como entradas.
Las búsquedas y parámetros exactos están en los JSON/CSV de resultados.

## Funciones y archivos compartidos

`guardar_metricas(..., archivo="metricas_izan.csv")` escribe por persona y
evita duplicados experimento/nivel/conjunto. Sin `archivo` sigue usando
`metricas.csv`, conservando las llamadas antiguas.
`guardar_predicciones(experimento, nivel, conjunto, conjuntos, y_pred)` genera
el esquema `projectID,nivel,conjunto,y_real,y_pred` que consume Sara.
`evaluar(y_real, y_pred, clases=...)` usa accuracy y macro-F1 con clases fijas.
`cargar_representacion(nombre, conjuntos)` verifica datos, filas y orden.

Los Excel, entornos, matrices y modelos quedan fuera de GitHub. Para repetir
la evaluación original se necesitan `datos/cache/{tfidf,word2vec,bert}.joblib`
y `datos/cache/modelos_izan/`.
Los CSV y gráficas bastan para que Sara integre mi comparación sin esas cachés.

El cuaderno se entrega con `EVALUAR_TEST=True`, `SOLO_MODELOS_ELEGIDOS=True` y
`FORZAR_ENTRENAMIENTO=False`. Se detiene si falta un modelo compatible.
Para reproducir entrenamiento y validación desde cero, hacerlo en un clon sin modelos
con las dos primeras opciones en False; se omiten los apartados finales de test.
No sustituir el cierre original ni usar el test conocido para nuevos ajustes.
Las versiones efectivas están en `resultados/entorno_izan.json`.

## Cómo continuar

Leer el README, mi cuaderno, `funciones.py` y `resultados/README.md`.
Mi código y mis resultados están completados; no comenzar de nuevo las tareas
de las guías antiguas. Comprobar los cambios posteriores de Git antes de actuar.
Lo siguiente para el grupo es reunir mi entrega con Sara y terminar su test.
Las diapositivas se prepararán cuando se soliciten.

No crear commits, push, firmas ni líneas `Co-authored-by` de IA. Izan hace la
subida con su propia identidad. Las ayudas académicas se reconocen en el README.
Al terminar, explicar qué archivos se cambiaron y qué se ejecutó realmente,
con lenguaje sencillo y sin presentar como terminado el trabajo de otra persona.
