# Resultados

- `particiones.csv`: proyectos de train, validación y test, con su orden y etiquetas.
- `metricas.csv`: métricas que van guardando los cuadernos. Empieza sin resultados.
- `graficas/`: figuras que se incluirán en el README.
- `predicciones/`: predicciones finales, identificadas por `projectID`.

El reparto usa el 60 % para entrenamiento, el 30 % para validación y el 10 % para
test, con semilla 42 y estratificación por categoría de nivel 2, como en el
cuaderno original. No cambiarlo por separado en cada cuaderno.

Está pendiente explicar la diferencia entre el porcentaje conservado actual
y el punto de control aproximado del enunciado. Si esa revisión cambia las
etiquetas o los proyectos, se deberá regenerar el reparto entre todos y repetir
los experimentos afectados.

Los hiperparámetros se eligen con validación. Las métricas de test se calculan
cuando estén cerradas las decisiones de modelado.
