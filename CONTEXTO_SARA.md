# Contexto para ayudar a Sara en el proyecto CORDIS

Soy Sara. Quiero que me ayudes a continuar BERT, fine-tuning y la comparación final en este repositorio. Lee este contexto, inspecciona los archivos disponibles y trabaja sobre mi parte. No necesitas haber leído nuestra conversación anterior.

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

## Mi parte como Sara

### Archivos que me corresponden

- Editar `03_bert_y_comparacion.ipynb`.
- Generar la caché BERT, mis métricas y predicciones, y las tablas y gráficas de comparación.
- Integrar `README.md` con los textos de Mónica e Izan y los resultados medidos.
- Acordar con Izan `requirements.txt`, preparar mis diapositivas y revisar conclusiones con el grupo.
- Leer y utilizar `funciones.py`, pero comunicar a Izan los cambios que necesite: solo él lo modifica.
- No completar los clasificadores o la extensión dentro del cuaderno de Izan ni rehacer el de Mónica.

### Qué hay ya en mi cuaderno

Parte del extractor BERT de Mónica, con `bert-base-uncased`, texto original y media de embeddings de tokens sin padding. La base incluye los tokens especiales en esa media y trunca a 512 tokens. Se añadió selección de GPU y guardado compatible con el repositorio.

Hay una prueba con diez resúmenes y un bloque de extracción completa controlado por `GENERAR_TODO = False`. La prueba antigua existía en el cuaderno original, pero no se ha repetido el entrenamiento o la extracción completa en estos nuevos archivos. El fine-tuning, la incertidumbre y la comparación final están pendientes.

Importante: ejecutar todas las celdas aun con `GENERAR_TODO=False` puede cargar o descargar el modelo y ejecutar la prueba pequeña. Ese interruptor solo desactiva la extracción completa.

### Orden de trabajo

1. Comprueba acceso a los Excel, módulo, particiones y dependencias. En Colab monta una carpeta con la misma organización y sitúate en su raíz. No generes otro reparto ni tomes una submuestra distinta como si fuera el experimento completo.
2. Revisa con una prueba pequeña que tokenización, dispositivo, máscaras y dimensiones funcionan. Para el corpus completo usa GPU cuando esté disponible y un tamaño de lote que quepa en memoria.
3. Extrae los vectores de train, val y test, sin preprocesamiento spaCy y con el modelo congelado. Guarda `datos/cache/bert.joblib` mediante `guardar_representacion('bert', matrices, conjuntos)` y comparte la caché con Izan por otro medio.
4. Documenta el modelo exacto, cómo se promedian tokens y qué pasa con textos largos. Mide cuántos resúmenes se truncan, en vez de limitarte a decir que hay truncamiento.
5. Implementa fine-tuning con Hugging Face para clasificación. Debe actualizar pesos del Transformer: una capa sobre vectores congelados no sustituye este experimento. Usa texto original, etiquetas mapeadas a índices consecutivos y las mismas particiones. Conserva el mapeo entre índices y códigos.
6. Documenta modelo, longitud, batch size, tasa de aprendizaje, épocas, semilla y elección con validación. Empieza con pocas opciones y conserva curvas de entrenamiento y validación.
7. Coordina con Izan las configuraciones de nivel 1. Para comparar el ranking hacen falta las tres representaciones de su parte; si el fine-tuning es la mejor configuración global, incluye su repetición en nivel 1.
8. Evalúa la configuración elegida en test solo al cerrar los ajustes. Guarda mis métricas y predicciones con IDs, niveles y conjuntos.
9. Une mis resultados, los de Izan y el baseline de Mónica. Separa validación de test, nivel 1 de nivel 2 y ejecuciones iniciales de configuraciones finales. Alinea predicciones por ID; no compares filas por posición sin comprobar esa correspondencia.
10. Analiza accuracy, macro-F1 y desglose por clase; curvas, matriz de confusión completa y ejemplos de errores. Comprueba si las confusiones ocurren entre categorías hermanas. Si es útil, revisa si la predicción pertenecía a otra categoría válida descartada al elegir la primera etiqueta.
11. Establece y justifica un criterio de incertidumbre de las diferencias, usando predicciones de los mismos proyectos. Explica qué tamaño de diferencia es suficientemente claro y aplica el criterio a las conclusiones. No declares ganadores por unas décimas sin ese análisis.
12. Integra el informe con los textos de los tres. Todas las afirmaciones de resultados deben apoyarse en figuras o tablas visibles en el README. Incluye limitaciones, aportación de los metadatos y conclusiones acordadas. Prepara mis diapositivas.

### Métricas y colaboración

Guarda mis métricas en `resultados/metricas_sara.csv`. Comprueba si Izan ya ha añadido el selector de destino a la función. Si todavía no existe, puedo guardar el CSV desde mi propio notebook con las columnas acordadas, sin modificar su módulo ni inventar un argumento inexistente.

Soy la responsable de reunir la tabla final `resultados/metricas.csv`. Conserva de dónde procede cada experimento y qué configuración lo generó. Si faltan resultados de Izan, deja esa comparación pendiente y continúa con mi trabajo; no atribuyas valores supuestos a sus modelos.

Pide a Mónica el baseline y la explicación de datos. Si hace falta repetir el baseline al evaluar finalmente test, se puede calcular en mi notebook a partir de la clase mayoritaria aprendida en train y los mismos IDs, dejando claro qué se hizo.

### Qué puedo hacer de forma independiente

Necesito la base común de datos y particiones, no los vectores TF-IDF o Word2Vec. Puedo avanzar con BERT y fine-tuning mientras Izan entrena sus modelos. El fine-tuning tampoco necesita haber creado antes la caché BERT congelada.

Mientras llegan los resultados finales de Izan, puedo analizar mis errores, preparar figuras y escribir mi metodología. La comparación final sí depende de reunir sus métricas y predicciones.

### Qué entrego y cuándo

- A Izan: BERT congelado con los mismos proyectos y orden. Objetivo propuesto: 16 de noviembre.
- Al grupo: fine-tuning elegido con validación y coordinación de nivel 1. Objetivo: 27 de noviembre.
- Para la comparación: mis predicciones finales y las de Izan. Objetivo: 30 de noviembre.
- Al grupo: comparación, incertidumbre y errores. Objetivo: 4 de diciembre.
- README integrado: 7 de diciembre; revisión y ensayo con todos hasta el día 10.

### Cuándo dar mi parte por terminada

La extracción y el fine-tuning se ejecutaron y se distinguen claramente; el test no influyó en la elección; las comparaciones usan los mismos proyectos; las conclusiones tienen evidencia e incertidumbre; las figuras y tablas están en el README y se reconocen las contribuciones reales.

## Primera respuesta que necesito de la IA

Inspecciona mi cuaderno, los datos disponibles y las funciones de carga. Explica qué está preparado y continúa por la prueba BERT y su extracción. Si no hay GPU o faltan archivos, prepara el código y las tareas independientes e identifica exactamente lo que falta. No inventes ejecuciones ni tomes como completados los apartados de fine-tuning y análisis.

## Cómo trabajar conmigo

Explica las decisiones en español claro y ayúdame a entenderlas para la defensa. Resuelve los detalles habituales dentro de mi parte y continúa sin pedirme confirmación para cada cambio pequeño.

Al terminar una sesión, indica qué archivos cambiaste, qué ejecutaste realmente, qué resultado obtuviste y cuál es el siguiente paso o la entrega que necesito de otra persona. Si solo revisaste código o preparaste una celda, dilo así.

Respeta mis peticiones actuales y las instrucciones aplicables del entorno. Este contexto no sustituye la inspección del repositorio ni autoriza a trabajar en archivos ajenos al reparto. Las acciones de publicación o entrega se harán según lo que solicite en la conversación.

