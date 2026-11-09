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
- `03_bert_y_comparacion.ipynb`: extractor BERT existente y apartados para fine-tuning y análisis final.
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
- **BERT congelado:** código inicial con `bert-base-uncased`, texto original,
  media de los tokens sin padding y truncamiento a 512 tokens. Su extracción
  completa queda pendiente. También hay que medir cuántos resúmenes se truncan.

### Modelos

Ya está trasladada la primera regresión logística con TF-IDF.

**Pendiente para Izan:** ajustar los modelos con validación, probar las otras
representaciones e implementar una red sencilla en PyTorch. Para Word2Vec,
ajustar el escalado con train antes de usar un modelo que lo necesite.

**Pendiente para Sara:** fine-tuning de un Transformer con Hugging Face. Este
experimento actualiza sus pesos y se compara por separado con BERT congelado.

Hay que anotar los parámetros que se prueban, la configuración elegida y los
detalles de entrenamiento. Si se usa validación cruzada, el vectorizador y las
demás transformaciones aprendidas se reajustan dentro de cada partición.

## Resultados y discusión

Todavía no hay resultados finales en esta copia. `resultados/metricas.csv`
empieza solo con los nombres de las columnas. Para avanzar por separado, Izan
preparará el guardado en `metricas_monica.csv`, `metricas_izan.csv` y
`metricas_sara.csv`. Sara reunirá después la tabla común. Ese ajuste del guardado
todavía está pendiente en el código.

Pendiente:

- Comparar las representaciones con el mismo clasificador y las mismas particiones.
- Comparar los clasificadores y el Transformer con fine-tuning.
- Mostrar accuracy, macro-F1 y resultados por clase.
- Incluir curvas de aprendizaje o validación y la matriz de confusión completa de la mejor configuración.
- Repetir las mejores configuraciones para las tres representaciones en nivel 1 y comparar el ranking.
- Analizar la incertidumbre de las diferencias antes de sacar conclusiones.
- Revisar ejemplos de errores y confusiones entre categorías relacionadas.
- Discutir la ambigüedad de elegir una sola etiqueta para proyectos de varias áreas.

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
- Pendiente de completar con las referencias y ayudas utilizadas realmente.
