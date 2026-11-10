# Proyecto CORDIS

Trabajo de Tratamiento de Datos sobre clasificación de proyectos de investigación.
Queremos predecir el área científica de un proyecto a partir de su resumen y
comparar distintas representaciones y modelos.

**Estado:** base inicial organizada a partir del cuaderno que ya había hecho una
persona del grupo. Los apartados marcados como pendientes se completarán al
realizar los experimentos; todavía no hay una comparación final.

## Cómo nos repartimos

Mónica hizo el cuaderno original, incluidos el inicio de la regresión logística
y el extractor BERT. Esa aportación sigue siendo suya aunque el código esté
repartido entre los tres cuadernos. Su carga nueva será menor para reconocer
ese trabajo previo.

| Persona | Archivos principales | Trabajo pendiente |
| --- | --- | --- |
| Mónica | `01_datos_y_representaciones.ipynb` | Revisar datos y etiquetas, generar TF-IDF y Word2Vec y explicar la exploración |
| Izan | `02_modelos_y_extension.ipynb` y `funciones.py` | Mantener las funciones, ajustar clasificadores, hacer la red y la extensión |
| Sara | `03_bert_y_comparacion.ipynb` | Completar BERT, hacer fine-tuning y comparar los resultados |

**Solo Izan edita `funciones.py`.** Mónica y Sara le comunican los ajustes que
necesiten. Los tres escriben sus apartados del README y preparan sus diapositivas.
Sara reúne el informe e Izan reúne las diapositivas. Las conclusiones se revisan
entre los tres. La declaración final de contribuciones reflejará lo que se haga
realmente, sin tratar la plantilla o los apartados pendientes como trabajo terminado.

El reparto detallado, las dependencias y el Gantt están en
`Reparto_y_calendario_CORDIS.pdf`.

## Qué hay en cada archivo

- `01_datos_y_representaciones.ipynb`: preparación, exploración, TF-IDF y Word2Vec.
- `02_modelos_y_extension.ipynb`: primera regresión logística y apartados para completar los otros modelos y la extensión.
- `03_bert_y_comparacion.ipynb`: BERT congelado, fine-tuning de BERT, tabla común de resultados, incertidumbre y análisis de errores.
- `funciones.py`: funciones que comparten los cuadernos; responsable único: Izan.
- `datos/`: Excel y vectores locales; quedan fuera de GitHub.
- `resultados/`: reparto de proyectos, métricas, predicciones y gráficas.
- `presentacion.md`: guion inicial para preparar las diapositivas.

El cuaderno original se conserva en su ubicación inicial fuera de esta carpeta.
El código existente de preparación, representaciones, BERT y primera regresión
logística se ha repartido entre estos archivos. Las salidas de los nuevos
cuadernos se han limpiado para no presentar resultados antiguos como actuales.

## Problema y datos

El conjunto original contiene 35.378 proyectos H2020. Utilizamos `summary` como
entrada del proyecto básico y construimos la etiqueta con `euroSciVocCode` y el
catálogo `SciVocCodes.xlsx`.

Para cada proyecto recorremos sus códigos en el orden disponible y elegimos el
primero cuyo camino tenga una categoría de nivel 2. Guardamos esa categoría y su
raíz de nivel 1. Descartamos proyectos sin una categoría válida.

La preparación actual conserva 31.982 proyectos (90,40 %), con 39 categorías de
nivel 2 y 6 de nivel 1. El reparto guardado contiene 19.189 proyectos de
entrenamiento, 9.594 de validación y 3.199 de test.

**Pendiente:** explicar la diferencia entre el porcentaje conservado que se
obtiene con la preparación actual y el 90,31 % aproximado indicado en el
enunciado. No se ha modificado la regla para forzar ese porcentaje.

El análisis exploratorio incluye valores ausentes, clases y desbalance, un
clasificador que siempre predice la clase mayoritaria, longitud de resúmenes,
proyectos por año y país, palabras frecuentes y ejemplos de proyectos.

**Pendiente:** incluir aquí las figuras y explicar las observaciones principales.
Las gráficas deben poder verse en este README sin ejecutar los cuadernos.

## Método

### Entrenamiento, validación y test

Se mantiene el reparto del cuaderno original: 60 % entrenamiento, 30 % validación
y 10 % test, con semilla 42 y estratificación por la etiqueta de nivel 2.
`resultados/particiones.csv` guarda los identificadores, etiquetas y orden.
Los tres cuadernos reutilizan ese archivo y avisan si los datos ya no coinciden.

El vocabulario, los embeddings entrenados con el corpus, la imputación y el
escalado se ajustan únicamente con entrenamiento. Los hiperparámetros se eligen
con validación; el test se reserva para el final.

### Representaciones

- **TF-IDF:** lematización con spaCy, minúsculas y eliminación de stopwords,
  números y tokens de hasta dos caracteres. Como configuración inicial:
  `max_features=10000`, `min_df=5`, `max_df=0.90` y unigramas/bigramas.
- **Word2Vec:** entrenado únicamente con los textos de entrenamiento. La base
  usa 300 dimensiones, ventana 5, `min_count=2`, skip-gram y 10 épocas.
  Usamos un trabajador y semilla 42 para facilitar la repetición. Promediamos
  las palabras conocidas; si no hay ninguna, devolvemos ceros. El cuaderno
  calcula cuántas palabras quedan fuera de vocabulario y cuántos documentos
  carecen de un vector utilizable.
- **BERT congelado (Sara):** `bert-base-uncased` usado solo como extractor de
  características: modo evaluación, sin gradientes y con los pesos sin cambiar. La
  entrada es el `summary` original, sin el preprocesamiento de spaCy, porque BERT
  tiene su propio tokenizador y aprovecha el contexto completo. Cada resumen se
  representa con la **media de los vectores de la última capa** de todos sus tokens
  reales: la máscara de atención excluye el padding, y la media incluye `[CLS]` y `[SEP]`.
  Así se obtienen 768 dimensiones. Se prefiere la media al vector de `[CLS]` porque, sin
  fine-tuning, `[CLS]` no está entrenado para resumir el documento.
  Los textos de más de 512 tokens se truncan. Lo hemos **medido**: la mediana es de
  366 tokens, el percentil 95 de 423, y solo 28 de 31.982 resúmenes (0,09 %) superan
  el límite, así que no compensa dividirlos en ventanas. La extracción completa
  tardó 16,5 minutos en una GPU T4 (configuración en
  `resultados/bert_congelado_config.json`). Los vectores se guardan en
  `datos/cache/bert.joblib`, fuera de GitHub, con una huella que comprueba los proyectos y su orden.

### Modelos

Ya está trasladada la primera regresión logística con TF-IDF.

**Pendiente para Izan:** ajustar los modelos con validación, probar las otras
representaciones e implementar una red sencilla en PyTorch. Para Word2Vec,
ajustar el escalado con train antes de usar un modelo que lo necesite.

**Fine-tuning de BERT (Sara).** A diferencia de BERT congelado, aquí se
actualizan todos los pesos del Transformer con las etiquetas del problema. Se usa
`AutoModelForSequenceClassification` de Hugging Face: el mismo `bert-base-uncased`
más una capa lineal sobre `[CLS]`. Usar el mismo modelo base que en la versión
congelada permite atribuir la diferencia a la adaptación de los pesos.

- Entrada: el `summary` original, `max_length=512` (truncamiento despreciable,
  ver arriba) y padding por lote. Mismas particiones que el resto del grupo.
- Etiquetas: los códigos EuroSciVoc se convierten en índices 0…K−1 con las clases de
  train. El mapeo se guarda en `resultados/finetuning_mapeo_nivel{N}.json`.
- Entrenamiento: AdamW, lote 16, 3 épocas, decaimiento de pesos 0,01, calentamiento
  lineal del 10 % de los pasos, fp16 y semilla 42, en una GPU T4 de Colab. Estos
  valores están dentro de los rangos que recomiendan Devlin et al. (2019) para BERT.
- Selección: evaluación en validación al final de cada época, conservando la de
  mejor macro-F1. Entre tasas de aprendizaje también se elige por macro-F1 en
  validación. El test no interviene.

| Tasa de aprendizaje | Épocas | Mejor época | Accuracy val | Macro-F1 val | Minutos |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 2e-5 | 3 | 3 | 0,573 | 0,338 | 29,5 |
| 3e-5 | 3 | 3 | 0,585 | 0,370 | 32,0 |

Configuración elegida: **tasa 3e-5**, por tener el mejor macro-F1 en validación. Su
ventaja sobre 2e-5 (+0,031 de macro-F1) es significativa según el bootstrap pareado
(IC 95 % de la diferencia: 0,023 a 0,040). Como esta misma validación se usó para
elegir, la cifra de la configuración elegida puede ser algo optimista; la estimación
sin sesgo será la de test. Detalle en
`resultados/finetuning_busqueda_nivel2.csv`; historiales completos en
`resultados/finetuning_bert_*_historial.json`.

Hay que anotar los parámetros que se prueban, la configuración elegida y los
detalles de entrenamiento. Si se usa validación cruzada, el vectorizador y las
demás transformaciones aprendidas se reajustan dentro de cada partición.

## Resultados y discusión

> **Estado:** resultados **provisionales, en validación**. Todavía faltan los
> modelos ajustados de Izan y la evaluación final en test, que se hará con las
> decisiones cerradas.

La tabla común `resultados/metricas.csv` la genera el cuaderno 03. Reúne
`metricas_monica.csv`, `metricas_izan.csv` y `metricas_sara.csv`, si existen, y el
baseline de clase mayoritaria calculado con los mismos proyectos.

### Fine-tuning de BERT (validación)

| Modelo | Nivel | Accuracy val (IC 95 %) | Macro-F1 val (IC 95 %) |
| --- | ---: | --- | --- |
| BERT fine-tuning, tasa 3e-5 (elegida) | 2 | 0,585 (0,575–0,594) | 0,370 (0,358–0,380) |
| BERT fine-tuning, tasa 2e-5 | 2 | 0,573 (0,562–0,581) | 0,338 (0,328–0,347) |
| Baseline: clase mayoritaria | 2 | 0,108 (0,102–0,114) | 0,005 (0,005–0,005) |
| BERT fine-tuning, tasa 3e-5 | 1 | 0,715 (0,706–0,724) | 0,676 (0,662–0,689) |
| Baseline: clase mayoritaria | 1 | 0,392 (0,382–0,402) | 0,094 (0,092–0,096) |

Los intervalos son bootstrap con 1.000 remuestreos de los proyectos de validación.

![Curvas de entrenamiento y validación](resultados/graficas/finetuning_bert_n2_lr3e-05_curvas.png)

**Lectura de las curvas:** la pérdida de validación baja en las tres épocas y el
macro-F1 sigue subiendo al final, así que no hay sobreajuste. Con más épocas
quizá mejorase un poco.

### Incertidumbre y criterio para comparar

Con un único conjunto de evaluación, las métricas dependen de qué proyectos han
caído en él. Para la accuracy, la mitad del intervalo del 95 % es aproximadamente
**±1 punto en validación (9.594 proyectos) y ±1,7 puntos en test (3.199)**. El
macro-F1 es más ruidoso, porque varias clases tienen muy pocos ejemplos: la clase 41
tiene 2 en validación y 1 en test. Para comparar dos modelos usamos un **bootstrap
pareado**: en cada remuestreo, los mismos proyectos para los dos modelos, unidos por
`projectID`. Una diferencia solo se considera real si su intervalo del 95 % **no
contiene el 0**. Si lo contiene, se informa como empate. Los resultados están en
`resultados/intervalos_val.csv` y `resultados/diferencias_val.csv`.

### Dónde falla el modelo (finetuning_bert_n2_lr3e-05, validación)

![F1 por clase](resultados/graficas/f1_por_clase_finetuning_bert_n2_lr3e-05_val.png)

- **Clases pequeñas:** 9 de las 39 categorías tienen F1 = 0, y todas tienen como mucho
  39 ejemplos en validación. Son categorías como ingeniería química, ingeniería
  médica, biotecnología industrial o ciencias veterinarias. El modelo prácticamente no
  llega a predecirlas, y eso explica que el macro-F1 (0,370) quede tan por debajo de la
  accuracy (0,585).

![Matriz de confusión normalizada](resultados/graficas/confusion_finetuning_bert_n2_lr3e-05_val.png)

- **Confusiones entre categorías relacionadas:** el 33,8 % de los errores
  cae en una categoría hermana (misma raíz de nivel 1). Si el modelo eligiese la
  categoría equivocada al azar, con la frecuencia con que predice cada una, sería
  el 21,1 %. Las confusiones más frecuentes son entre medicina
  básica, medicina clínica y ciencias biológicas, y entre informática e ingeniería
  eléctrica y electrónica. Varias de estas parejas tienen raíces distintas en EuroSciVoc
  (por ejemplo, informática está en ciencias naturales e ingeniería eléctrica en
  ingeniería), pero sus temas están muy próximos en la práctica.
- **Ambigüedad de la etiqueta:** el **55,1 % de los errores** consiste
  en predecir otra de las categorías válidas del proyecto, que descartamos al quedarnos
  solo con la primera. Si esas predicciones contaran como acierto, la accuracy pasaría
  de 0,585 a **0,814**. Una parte grande del error medido
  se debe, por tanto, a la elección de una sola etiqueta y no a un fallo real del
  modelo, lo que confirma el techo del que habla el enunciado.

Detalle por clase y lista de errores en `resultados/por_clase_*_val.csv` y
`resultados/errores_*_val.csv`.

### Nivel 1: seis categorías (finetuning_bert_n1_lr3e-05, validación)

Se repitió la mejor configuración (tasa 3e-5) con las 6 raíces de EuroSciVoc.

![Curvas nivel 1](resultados/graficas/finetuning_bert_n1_lr3e-05_curvas.png)

- El macro-F1 pasa de 0,370 (39 clases) a **0,676** (6 clases), y la
  accuracy de 0,585 a **0,715**. Con categorías más amplias hay muchos
  más ejemplos por clase y desaparecen las clases casi vacías: el F1 por clase va de
  0,53 (ciencias agrícolas, la raíz más pequeña) a 0,75.
- La pérdida de validación sube ligeramente en la tercera época (0,809 → 0,762 → 0,796), aunque el
  macro-F1 sigue mejorando. Se conserva la época 3 porque el criterio de selección es
  el macro-F1.
- El **62,3 % de los errores** es otra raíz válida del proyecto. Si esas
  predicciones contaran como acierto, la accuracy sería 0,893. Las confusiones más
  frecuentes son entre ciencias naturales e ingeniería, en los dos sentidos, y entre
  ciencias naturales y medicina: áreas muy solapadas en proyectos interdisciplinares.
- **Ranking de representaciones:** la comparación de TF-IDF, Word2Vec y BERT congelado en
  los dos niveles queda pendiente de los resultados de Izan. El cuaderno 03 la calcula
  automáticamente en cuanto existan sus métricas.

Pendiente:

- Comparar las representaciones con el mismo clasificador y las mismas particiones.
- Comparar los clasificadores y el Transformer con fine-tuning.
- Mostrar accuracy, macro-F1 y resultados por clase.
- Incluir curvas de aprendizaje o validación y la matriz de confusión completa de la mejor configuración.
- Repetir las mejores configuraciones para las tres representaciones en nivel 1 y comparar el ranking.
- Aplicar el criterio de incertidumbre a la comparación final (el método ya está en el cuaderno 03).
- Repetir el análisis de errores en test para la mejor configuración final.

## Extensión

La propuesta es comparar un modelo que use solo texto, otro que use solo
metadatos y otro que combine ambas cosas. Mantendremos las mismas particiones.

Se pueden usar coste, financiación europea, duración, país coordinador y número
de países participantes. Las etiquetas y los códigos EuroSciVoc no son entradas.
Las imputaciones, la codificación de países y el escalado se aprenden con train.

**Pendiente:** implementación, tablas, gráficas y discusión.

## Conclusiones y limitaciones

Pendiente de completar con los resultados medidos. Hay que explicar tanto lo
que funciona como lo que no, el efecto del desbalance y la ambigüedad de las
etiquetas. La calidad del trabajo depende de la metodología y del análisis,
no de alcanzar una accuracy concreta.

## Para ejecutar

Abrir una terminal en esta carpeta y usar un entorno de Python compatible con
las dependencias; Python 3.12 es una opción para empezar:

```powershell
python -m pip install -r requirements.txt
python -m spacy download en_core_web_sm
python -m jupyter lab
```

El comando `python` debe corresponder al entorno en el que se quiera trabajar.
Los dos Excel van en `datos/`. Consultar `datos/README.md`.

1. Acordar los datos y las particiones; Izan revisa las funciones comunes.
2. Mónica ejecuta el cuaderno 1 y Sara puede ejecutar el 3 en paralelo: BERT
   necesita los resúmenes originales, no los vectores de Mónica.
3. Izan prepara su código y los metadatos desde el principio y ejecuta los
   clasificadores conforme recibe los vectores de Mónica y Sara.
4. Sara hace fine-tuning en paralelo a los modelos de Izan y reúne al final
   las comparaciones. La evaluación final en test se hace tras cerrar los ajustes.

Las partes pendientes están escritas como tareas. El cálculo completo de BERT
requiere activar `GENERAR_TODO` en su cuaderno. No hace falta ejecutarlo para
abrir el proyecto. Para Colab hay que proporcionar los mismos datos,
`funciones.py` y el CSV de particiones, y situarse en la carpeta del proyecto.

`requirements.txt` es una lista inicial; antes de entregar hay que guardar las
versiones del entorno con el que se hayan reproducido los experimentos finales.

## Organización y entrega

Cada uno trabaja principalmente en su cuaderno. Antes de empezar descarga los
cambios del grupo y, cuando tenga una parte que funcione, la sube con un mensaje
corto. Solo Izan modifica `funciones.py` y avisa al resto si cambia su uso.

El repositorio debe ser público. La entrega es el 11 de diciembre de 2026 a las
23:59. Una persona sube a Aula Global el enlace, las contribuciones reales de
cada miembro y las diapositivas. La presentación y defensa son individuales.

## Fuentes y ayudas utilizadas

- Enunciado del proyecto CORDIS de la asignatura.
- Datos H2020 y catálogo EuroSciVoc proporcionados para el trabajo.
- Cuaderno inicial realizado por Mónica.
- Devlin, J., Chang, M.-W., Lee, K. y Toutanova, K. (2019). *BERT: Pre-training of Deep
  Bidirectional Transformers for Language Understanding*. NAACL-HLT. Modelo
  `bert-base-uncased` y rangos de hiperparámetros para el fine-tuning.
- Biblioteca Hugging Face Transformers (`AutoModel`, `AutoModelForSequenceClassification`, `Trainer`).
- Sara utilizó un asistente de IA (Claude, de Anthropic) como ayuda para preparar y
  revisar el código y los textos de su parte. Todos los resultados proceden de
  ejecuciones reales, registradas en `resultados/`.
- Pendiente de completar con las referencias y ayudas utilizadas por el resto del grupo.
