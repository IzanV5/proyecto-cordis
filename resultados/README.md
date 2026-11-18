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

## Comparación común (Sara)

`metricas_sara.csv`, `metricas.csv`, `intervalos_val.csv`, `diferencias_val.csv`
y los resultados de fine-tuning conservan el contenido de Sara. El cuaderno 03
reúne los CSV personales. La comparación conjunta en test necesita incorporar
las predicciones del fine-tuning sobre esos mismos 3.199 proyectos; no comparar
sus métricas de validación con las métricas de test de Izan.
