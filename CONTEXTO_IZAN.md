# Contexto para ayudar a Izan en el proyecto CORDIS

Soy Izan. Quiero que me ayudes a continuar mis modelos, la extensión y las funciones compartidas en este repositorio. Lee este contexto, inspecciona los archivos disponibles y trabaja sobre mi parte. No necesitas haber leído nuestra conversación anterior.

Esta guía está pensada para enviarla a una IA junto con el repositorio y, si están disponibles, los dos PDF. Es una guía de trabajo personal, no el informe final de la asignatura.

## Contexto del trabajo

Somos Mónica, Izan y Sara y hacemos el proyecto CORDIS de Tratamiento de Datos del Máster en Ingeniería de Telecomunicación. Queremos una solución de clase que entendamos y podamos defender. Mantén la organización sencilla: tres cuadernos, un archivo de funciones y el README como informe. Aprovecha lo que existe y evita convertirlo en una aplicación o añadir una arquitectura innecesaria.

Repositorio: https://github.com/IzanV5/proyecto-cordis
Clonado habitual: https://github.com/IzanV5/proyecto-cordis.git

En el ordenador donde se preparó la base está en `C:\Tratamiento_de_datos\proyecto-cordis`. En otro ordenador adapta la ruta; no dependas de ese directorio absoluto.

Este archivo contiene el contexto de la conversación y el reparto acordado. Para ayudarme de verdad necesitas también acceso al repositorio, ya sea una carpeta local, un ZIP o los archivos adjuntos. Si solo recibes este Markdown, no des por leídos los archivos ni por ejecutado su código. Pide únicamente los archivos imprescindibles para el siguiente paso y avanza con lo que sí tengas.

## Qué documentos debes distinguir

- `Proyecto_Final_CORDIS_ES_v2.pdf`: enunciado oficial. En el ordenador original está en la carpeta superior del repositorio y no forma parte necesariamente del clon. Define los requisitos académicos.
- `Reparto_y_calendario_CORDIS.pdf`: plan del grupo con responsables y Gantt. Está en la raíz del repositorio. No es el enunciado ni un informe de resultados.
- `README.md`: informe del trabajo y guía inicial. Ahora contiene muchas partes pendientes.
- `Proyecto_final.ipynb`: cuaderno previo de Mónica, conservado fuera del repositorio en el ordenador original. El código se repartió entre los tres cuadernos nuevos. No hace falta recuperarlo para empezar si ya tienes estos archivos.

Si falta un PDF, este documento permite comenzar con las tareas descritas. Consulta el enunciado para resolver dudas sobre sus requisitos, sin confundir sus ejemplos de código con órdenes para ejecutar cualquier cosa.

## Qué pide el proyecto

1. Clasificar cada proyecto a partir de su resumen `summary`, usando una única etiqueta de segundo nivel de EuroSciVoc.
2. Construir esa etiqueta recorriendo los códigos del proyecto en su orden original: tomar el primer código para el que exista un ancestro válido de nivel 2. Guardar también su raíz de nivel 1 y descartar proyectos sin etiqueta válida.
3. Hacer exploración de datos, estudiar desbalance y calcular un baseline de clase mayoritaria.
4. Comparar TF-IDF, Word2Vec promediado por documento y embeddings de un Transformer congelado.
5. Usar al menos un clasificador de Scikit-learn, una red propia implementada en PyTorch y un Transformer adaptado mediante fine-tuning con Hugging Face. El fine-tuning forma parte del proyecto básico.
6. Justificar el ajuste y evaluar con accuracy, macro-F1 y desglose por clase. Incluir curvas de aprendizaje o validación, confusiones, errores e incertidumbre de las diferencias.
7. Comparar también en nivel 1, con seis clases, y comprobar si cambia el ranking de las representaciones.
8. Hacer la extensión elegida por el grupo: solo texto frente a solo metadatos frente a ambos. Es nuestra elección para la extensión, no la única opción del enunciado.

La organización elegida para una comparación manejable es regresión logística con las tres representaciones, una red pequeña de PyTorch empezando por Word2Vec y el fine-tuning por separado. No se ha acordado entrenar obligatoriamente todas las combinaciones posibles de red y representación.

Se valora la corrección metodológica y la explicación, no conseguir una accuracy concreta. Parte de las etiquetas procede de sugerencias automáticas revisadas por expertos. Además, muchos proyectos pertenecen a varias áreas y solo se elige la primera; hay que discutir esa ambigüedad.

La entrega es el **11 de diciembre de 2026 a las 23:59, hora de Madrid**. GitHub debe ser público y contener código reproducible y un README con el informe, las figuras y las tablas visibles sin ejecutar los cuadernos. Una persona entrega en Aula Global el enlace, las contribuciones reales y las diapositivas. La defensa es individual durante la semana del 14 de diciembre. El básico aporta hasta 2,25 puntos y la extensión hasta 0,75.

## Reparto que hay que respetar

| Persona | Su archivo principal | Otras responsabilidades |
| --- | --- | --- |
| Mónica | `01_datos_y_representaciones.ipynb` | Datos, etiquetas, exploración, TF-IDF y Word2Vec. |
| Izan | `02_modelos_y_extension.ipynb` | Clasificadores, red, extensión y mantenimiento exclusivo de `funciones.py`. |
| Sara | `03_bert_y_comparacion.ipynb` | BERT congelado, fine-tuning y comparación final. |

**Solo Izan modifica `funciones.py`.** Mónica y Sara pueden leerlo, usarlo y proponer un ajuste a Izan. No cambies sus funciones desde las tareas de ellas.

El contenido del README es de los tres. Cada persona prepara el texto de su parte, preferiblemente en su cuaderno; Sara lo integra en el informe. Izan y Sara acuerdan dependencias y versiones en `requirements.txt`. Izan mantiene `.gitignore` y reúne las diapositivas; cada uno prepara las suyas. Los tres revisan las conclusiones y ensayan.

## Estado comprobado al preparar estas guías

Referencia inicial: **9 de noviembre de 2026**. Comprueba los archivos actuales antes de actuar: puede haber trabajo posterior.

- Mónica aportó un cuaderno con preparación y exploración, código de TF-IDF y Word2Vec, una primera regresión logística con evaluación en validación y un extractor BERT probado con diez resúmenes.
- Esa autoría sigue siendo de Mónica aunque la regresión esté ahora en el cuaderno de Izan y BERT en el de Sara.
- Después se añadieron la organización, funciones compartidas y textos de tareas pendientes. Eso no equivale a que los experimentos estén completados.
- Los nuevos cuadernos se dejaron sin salidas ni contadores de ejecución. Se comprobaron sintaxis, preparación de datos y particiones; no se reentrenaron los modelos completos en la carpeta reorganizada.
- `resultados/metricas.csv` solo tenía la cabecera. No había comparación final, red propia, fine-tuning ni extensión implementados.
- No constaba una extracción BERT completa. No presentes como terminada una celda que solo contiene el código para hacerlo.
- El guardado por persona todavía es una tarea de Izan. La función actual `guardar_metricas` escribe en el archivo común, no admite todavía un argumento para elegir un CSV.

No uses un porcentaje de avance inventado ni atribuyas a una persona los archivos de apoyo o los apartados vacíos como si fueran trabajo académico terminado.

## Datos y particiones comunes

Los dos Excel se colocan localmente en `datos/projects.xlsx` y `datos/SciVocCodes.xlsx`. En el ordenador original proceden de `C:\Tratamiento_de_datos\H2020`. No están disponibles automáticamente al clonar; cada persona necesita sus copias.

La preparación actual dio:

| Comprobación | Valor |
| --- | ---: |
| Proyectos originales | 35.378 |
| Proyectos válidos | 31.982 |
| Conservados | 90,40 % |
| Categorías de nivel 2 | 39 |
| Categorías de nivel 1 | 6 |
| Entrenamiento | 19.189 |
| Validación | 9.594 |
| Test | 3.199 |

Se conserva el reparto del cuaderno original: 60 % train, 30 % val y 10 % test, semilla 42, estratificación por nivel 2. El CSV `resultados/particiones.csv` guarda `projectID,label_nivel1,label_nivel2,conjunto,orden`. Los conjuntos se llaman exactamente `train`, `val` y `test`. Se reutilizan en ambos niveles.

El enunciado da un 90,31 % aproximado de conservación. Mónica debe revisar y explicar la diferencia. No fuerces los datos a encajar con ninguno de estos números: son comprobaciones iniciales, no resultados que haya que imponer. Si cambia el criterio o los datos, hay que acordar un nuevo reparto y regenerar las representaciones y experimentos afectados.

`projectID` identifica proyectos y permite unir resultados; no es una variable predictiva. Conserva la lista original de códigos para poder estudiar categorías alternativas del mismo proyecto.

## Reglas de los experimentos

- Ajusta vocabulario, IDF, Word2Vec entrenado con el corpus, escalado, imputaciones y reducciones solo con entrenamiento.
- Elige hiperparámetros con validación. Si haces validación cruzada, reajusta las transformaciones aprendidas dentro de cada partición.
- Reserva el test para cuando estén cerradas las decisiones; no lo uses para elegir modelos o corregir su rendimiento.
- Usa las mismas instancias y etiquetas en las comparaciones. Mantén el orden al asociar filas de matrices con proyectos.
- Para macro-F1 y resultados por clase, utiliza un conjunto de clases de referencia consistente; no ocultes categorías pequeñas porque falten predicciones.
- Para BERT y fine-tuning utiliza texto original. El Transformer congelado y el fine-tuning son experimentos distintos.
- La extensión usa los mismos proyectos. No introduzcas EuroSciVoc, sus etiquetas o variables que las reproduzcan como entradas.
- Registra semilla, parámetros, tamaños, versiones y qué se ejecutó realmente. Guarda predicciones con identificador, etiqueta real, predicción y nivel. Indica la configuración y conjunto en el nombre del archivo.
- Una celda escrita, una comprobación de sintaxis y un entrenamiento completado son estados diferentes. No inventes métricas, salidas, figuras ni conclusiones.

## Archivos y funciones con los que continuar

Abre primero el README, el plan PDF, mi cuaderno y `funciones.py`. Las dependencias iniciales están en `requirements.txt`; aún no constituyen un entorno con versiones finales fijadas. Comprueba el Python activo y la disponibilidad de las bibliotecas y del modelo spaCy `en_core_web_sm`.

El módulo calcula las rutas a partir de su propio archivo, por lo que los cuadernos se abren desde la raíz del proyecto. En Colab también hay que colocar el módulo, los Excel y el mismo CSV de particiones.

Estas son las interfaces existentes; verifica que sigan siendo así:

```python
projects, scivoc = cargar_datos()
df = preparar_datos(projects, scivoc)
conjuntos = cargar_o_crear_particiones(df)
# conjuntos: {"train": DataFrame, "val": DataFrame, "test": DataFrame}

vectorizador, matrices = crear_tfidf(documentos, **parametros)
modelo_w2v, matrices, resumen_oov = crear_word2vec(documentos, **parametros)
# documentos: diccionario de listas de textos limpios con train, val y test
# matrices: diccionario con las mismas claves y filas en el orden de conjuntos

guardar_representacion("tfidf", matrices, conjuntos)
matrices = cargar_representacion("tfidf", conjuntos)
metricas = evaluar(y_real, y_predicha, clases=clases)
guardar_metricas(experimento, representacion, modelo, nivel, conjunto, metricas)
```


La función `preprocesar_resumenes(textos, nlp=None)` realiza la limpieza de texto utilizada por TF-IDF y Word2Vec. No se aplica al texto de BERT ni al fine-tuning.

Los nombres de las cachés son `tfidf`, `word2vec` y `bert`, y se guardan como `datos/cache/<nombre>.joblib`. Incluyen matrices y huellas que comprueban los datos y el orden. Utiliza las funciones al compartirlas. Si cambia el preprocesamiento o algún parámetro, regenera la representación, aunque las huellas de los datos coincidan.

El esquema de métricas existente es `experimento,representacion,modelo,nivel,conjunto,accuracy,macro_f1`. El plan es que cada persona genere `resultados/metricas_monica.csv`, `metricas_izan.csv` o `metricas_sara.csv`, y que Sara construya después la tabla común. Esos CSV personales se crearán al ejecutar, no se deben rellenar con resultados ficticios.

Los Excel, cachés, pesos y temporales quedan fuera de GitHub. Los vectores se comparten por otro medio o se regeneran con los mismos parámetros. Usa la identidad Git de la persona correspondiente; no añadas autores, firmas o líneas `Co-authored-by` de una IA. Las fuentes y contribuciones académicas se documentan según lo que se haya utilizado realmente.

## Calendario propuesto y dependencias

Son fechas internas propuestas, no constancia de entregas ya realizadas. Si se lee esto más tarde, comprueba qué existe y ajusta el trabajo pendiente con la fecha real.

| Fecha de 2026 | Entrega | Quién puede continuar |
| --- | --- | --- |
| 11 nov | Mónica e Izan acuerdan datos, particiones y uso de funciones | Mónica y Sara lanzan representaciones sobre la misma base. |
| 14 nov | Mónica entrega TF-IDF y Word2Vec | Izan entrena con esas representaciones. |
| 16 nov | Sara entrega BERT congelado | Izan completa la comparación con BERT. |
| 27 nov | Izan y Sara cierran configuraciones y comparaciones de nivel 1 | Pueden pasar a la evaluación final en test. |
| 30 nov | Izan y Sara entregan predicciones de test | Sara reúne comparación, incertidumbre y errores. |
| 4 dic | Sara prepara comparación final | Los tres revisan las conclusiones. |
| 7 dic | Informe conjunto completo | Revisión, diapositivas y ensayo hasta el día 10. |
| 11 dic | Entrega antes de las 23:59 | Izan reúne lo necesario para Aula Global. |

Sara puede hacer BERT y fine-tuning sin TF-IDF ni Word2Vec. Izan puede preparar funciones, red y metadatos mientras llegan las representaciones. La comparación definitiva sí requiere los resultados de los otros.

## Mi parte como Izan

### Archivos que me corresponden

- Editar `02_modelos_y_extension.ipynb`.
- Ser el **único editor de `funciones.py`** y mantener las interfaces que usan mis compañeras.
- Mantener `.gitignore` y acordar con Sara `requirements.txt`.
- Generar mis métricas, curvas y predicciones; preparar mi texto del informe y reunir las diapositivas.
- Recibir de Mónica los cambios acordados de datos y las cachés TF-IDF y Word2Vec; recibir BERT de Sara.
- No completar o reescribir los cuadernos de mis compañeras para dar por hecho su trabajo. Puedo enviarles ejemplos de uso o propuestas para que los apliquen en su parte.

### Qué hay ya en mi cuaderno y el módulo

El cuaderno contiene la regresión logística inicial de Mónica con TF-IDF, evaluación en validación, un informe por clase, guardado de predicciones y una matriz de confusión adaptada para mostrar todas las categorías. Los demás modelos, ajustes, nivel 1 y extensión son tareas pendientes.

El módulo ya tiene carga, preparación, particiones, preprocesamiento, representaciones, cachés con huellas y métricas. No tengo que crear todo ese archivo otra vez. Su preparación fue comprobada sobre los Excel, pero eso no demuestra que todos los entrenamientos y dependencias estén verificados.

### Primer trabajo en funciones.py

1. Revisa el código actual y conserva nombres, claves y retornos que usan los tres notebooks.
2. Aplica las correcciones de datos que acuerde con Mónica. No cambies unilateralmente el criterio de etiquetas ni el reparto.
3. Añade una forma de guardar en un CSV por persona. La firma actual es:
```python
guardar_metricas(experimento, representacion, modelo, nivel, conjunto, metricas)
```

   Todavía escribe siempre en `resultados/metricas.csv`. Puedes añadir un parámetro opcional al final y conservar el comportamiento de llamadas antiguas. Mantén las columnas acordadas y evita duplicar filas del mismo experimento, nivel y conjunto. Usa nombres de experimento distintos para cada configuración.
4. Pasa a Mónica y Sara un ejemplo exacto de la nueva llamada; no des por hecho que sus notebooks ya se han adaptado.
5. Comprueba que las particiones se recuperan en el mismo orden y que las cachés se guardan y cargan con las funciones existentes. Haz comprobaciones proporcionadas a los cambios, sin montar un sistema de pruebas innecesario.

### Orden de los experimentos

1. Continúa la regresión logística. Empieza con pocas opciones justificadas de regularización y, si procede, ponderación de clases. Usa macro-F1 en validación para elegir.
2. Repite el mismo clasificador con TF-IDF, Word2Vec y BERT congelado. Para las representaciones densas aplica el escalado que corresponda, ajustándolo con train.
3. Si ajustas la representación además del clasificador, vuelve a aprender esa representación solo con train y conserva sus parámetros. Coordina cambios del preprocesamiento con Mónica; no mezcles cachés de configuraciones diferentes.
4. Implementa una red pequeña con PyTorch, empezando por Word2Vec para no depender de BERT. No sustituyas este requisito por `MLPClassifier` de Scikit-learn. Documenta capas, activaciones, pérdida, optimizador, épocas, semillas y criterio de parada. Para clasificación, mapea los códigos de categoría a índices consecutivos y conserva el mapeo.
5. Prepara la extensión: costes, contribución UE, duración, país coordinador y número de países participantes. Trata ausentes y codificación de categorías con parámetros aprendidos en train. No utilices `projectID`, etiquetas, códigos EuroSciVoc o campos que reproduzcan el objetivo como variables predictivas.
6. Compara solo metadatos, solo texto y combinación con los mismos proyectos. Escoge la configuración de texto por validación y documenta qué modelo y representación empleas en cada caso.
7. Repite las configuraciones elegidas para las tres representaciones con `label_nivel1`, conservando las particiones. Pasa los resultados a Sara para comparar el ranking.
8. Cierra decisiones antes de la evaluación final en test. Guarda accuracy, macro-F1, desglose por clase, curvas de aprendizaje o validación y predicciones asociadas a `projectID`. Señala siempre nivel, conjunto y configuración.
9. Prepara mi parte del informe con las decisiones y resultados medidos, y comparte ese texto con Sara. Reúne las diapositivas de todos cuando estén listas.

### Cómo continuar sin esperar

- Antes de recibir vectores: funciones compartidas, código de entrenamiento, preparación de metadatos y estructura de la red.
- Con TF-IDF o Word2Vec: ejecutar sus clasificadores y entrenar la red con Word2Vec.
- Cuando llegue BERT: completar esa fila de la comparación con el mismo protocolo.
- Si falta una caché, no inventes sus matrices o métricas ni cambies el reparto para avanzar. Identifica la entrega pendiente y sigue con las tareas independientes.
- El fine-tuning de Sara no necesita mis clasificadores; solo la comparación final necesita reunir resultados.

### Qué entrego y a quién

- A ambas: funciones y modo de uso estables, con guardado por persona. Objetivo propuesto: 11 de noviembre.
- A Sara: configuraciones y resultados de validación de clásicos, red, extensión y nivel 1. Objetivo: 27 de noviembre.
- A Sara: `resultados/metricas_izan.csv` y predicciones finales con IDs. Objetivo: 30 de noviembre.
- Al grupo: explicación reproducible, versiones del entorno, mi texto y las diapositivas reunidas.

Antes de entregar, comprueba que una compañera puede ejecutar mis funciones y mi notebook siguiendo el README. El repositorio debe ser público y Aula Global recibe enlace, contribuciones reales y diapositivas; esta guía no implica que haya que publicar o entregar nada automáticamente.

### Cuándo dar mi parte por terminada

Las funciones siguen siendo utilizables por las dos compañeras; los modelos requeridos y la extensión están implementados y evaluados; las decisiones se tomaron sin test; configuraciones, métricas y predicciones son trazables; mis resultados están listos para el informe y puedo explicar el código.

## Primera respuesta que necesito de la IA

Inspecciona mi cuaderno y el módulo. Resume qué existe y empieza por mantener las interfaces y separar el guardado de métricas. Después continúa los modelos y la extensión, aprovechando las representaciones disponibles. No rehagas los otros cuadernos ni la estructura entera del proyecto.

## Cómo trabajar conmigo

Explica las decisiones en español claro y ayúdame a entenderlas para la defensa. Resuelve los detalles habituales dentro de mi parte y continúa sin pedirme confirmación para cada cambio pequeño.

Al terminar una sesión, indica qué archivos cambiaste, qué ejecutaste realmente, qué resultado obtuviste y cuál es el siguiente paso o la entrega que necesito de otra persona. Si solo revisaste código o preparaste una celda, dilo así.

Respeta mis peticiones actuales y las instrucciones aplicables del entorno. Este contexto no sustituye la inspección del repositorio ni autoriza a trabajar en archivos ajenos al reparto. Las acciones de publicación o entrega se harán según lo que solicite en la conversación.

