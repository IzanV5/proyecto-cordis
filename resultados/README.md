# Resultados

Los tres cuadernos usan `particiones.csv`: 19.189 proyectos de train, 9.594 de
validación y 3.199 de test, semilla 42 y estratificación por nivel 2. Las métricas
oficiales usan la primera etiqueta válida de cada proyecto y las mismas clases.

## Archivos de Izan (ejecución final: 18 de noviembre)

- `metricas_izan.csv`: 20 filas, diez configuraciones en validación y en test.
- `predicciones/izan_*_val.csv` y `izan_*_test.csv`: predicciones con esquema
  `projectID,nivel,conjunto,y_real,y_pred`; 9.594 o 3.199 filas por archivo.
- `izan_por_clase_*`: precision, recall, F1 y soporte, incluidas las clases con F1 cero.
- `busqueda_lr_izan.csv`, `busqueda_red_izan.csv` y `izan_mlp_*_historial.csv`:
  búsquedas y curvas del ajuste con validación.
- `configuraciones_izan.json` y `representaciones_izan_config.json`: parámetros elegidos.
- `entorno_izan.json`: versiones utilizadas realmente.
- `ranking_representaciones_izan_{val,test}.csv` y `extension_izan_{val,test}.csv`:
  comparaciones del mismo clasificador y de la extensión.
- `intervalos_izan_test.csv` y `diferencias_izan_test.csv`: bootstrap con 1.000
  réplicas, semilla 42, IC 95 % percentiles y clases fijas; diferencias A menos B.
- `resumen_errores_izan_test.csv` y `izan_errores_*_test.csv`: errores de TF-IDF,
  elegido con validación, y diagnóstico de categorías alternativas.
- `procedencia_representaciones_izan.json`: comprobación del ZIP de Mónica y la caché BERT de Sara.
- `cierre_modelos_izan.json`: huellas de modelos, matrices, particiones y configuraciones
  registradas antes de evaluar test.
- `comprobaciones_izan.json`: resumen de coherencia entre predicciones, etiquetas y métricas.
- `graficas/izan_*`: curvas, comparación, extensión y confusiones.

Las matrices y pesos están en `datos/cache/` y no se suben a GitHub. No hacen
falta para leer los resultados o para que Sara reúna las predicciones.

## Archivos de Sara (fine-tuning y comparación común)

- `bert_congelado_config.json`: configuración y duración de la extracción de BERT congelado.
- `metricas_sara.csv`: métricas de validación de todos los fine-tuning probados y de test de
  los dos elegidos (SciBERT con pesos en nivel 2, BERT original en nivel 1).
- `finetuning_busqueda_nivel{1,2}.csv`: configuraciones probadas, mejor época, duración y
  versiones de `torch` y `transformers`; `finetuning_*_historial.json`, historial por época;
  `finetuning_mapeo_nivel{1,2}.json`, correspondencia entre índices y códigos EuroSciVoc.
- `predicciones/finetuning_*_{val,test}.csv` y `predicciones/baseline_mayoritaria_*`: mismo
  esquema `projectID,nivel,conjunto,y_real,y_pred` que el resto del grupo.
- Comparación común, una versión por conjunto (`_val` con la que se decidió y `_test`, el
  informe final): `metricas.csv` (todas las métricas), `intervalos_{val,test}.csv`
  (bootstrap con 1.000 réplicas, semilla 42), `diferencias_{val,test}.csv` (bootstrap
  pareado por `projectID`; significativa si el IC 95 % no contiene 0),
  `ranking_representaciones_{val,test}.csv`, `resumen_errores_{val,test}.csv`,
  `por_clase_*` y `errores_*` (con la marca de si la predicción es otra categoría válida
  del proyecto).
- `graficas/`: curvas del fine-tuning, F1 por clase y matrices de confusión de los modelos
  analizados (`*_val.png` y `*_test.png`).

Los pesos de los modelos ajustados (unos 440 MB cada uno) no están en GitHub: SciBERT de
nivel 2 está en la salida de la ejecución de Kaggle y BERT de nivel 1 en Drive.
