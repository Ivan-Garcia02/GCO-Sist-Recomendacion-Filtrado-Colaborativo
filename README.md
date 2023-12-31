# Sistemas de recomendación. Métodos de filtrado colaborativo

### Iván García González y Daniel Jorge Acosta

## Instrucciones de instalación

Durante el desarrollo del proyecto no se ha hecho uso de ninguna librería externa, por lo que para su ejecución debería bastar con la instalación del intérprete de Python.

## Descripción del código

El código del proyecto se encuentra dividido en varios ficheros.

### file_reader

Contiene la función `read_file`, encargada de crear un array de dos dimensiones a partir del contenido del fichero de entrada. Además, controla que los valores de este array se encuentren entre el mínimo y el máximo establecidos en el fichero y que todas sus filas tengan la misma longitud. La matriz devuelta tendrá sustituidas las incógnitas por el valor -1.0 y sus valores se modificarán para que se sitúen en el intervalo [0.0, max - min], en lugar de [min, max], con el objetivo de facilitar el trabajo con esta.

### metrics

Este fichero contiene las funciones encargadas del cálculo de los grados de similaridad entre usuarios:

#### `pearson`

Esta función recibe dos vectores de valores flotantes que representan las valoraciones de dos usuarios y devuelve un valor entre -1 y 1 que representa la similaridad entre los mismos basándose en el coeficiente de correlación de Pearson. Para esto elimina las valoraciones que no hayan realizado ambos usuarios y calcula la similaridad basándose en el resto.

#### `cosine_similarity`

Esta función recibe dos vectores de valores flotantes que representan las valoraciones de dos usuarios y devuelve un valor entre -1 y 1 que representa la similaridad entre los mismos basándose en la distancia coseno. Para esto elimina las valoraciones que no hayan realizado ambos usuarios y calcula la similaridad basándose en el resto.

#### `euclidean_distance`

Esta función recibe dos vectores de valores flotantes que representan las valoraciones de dos usuarios y devuelve un valor entre -1 y 1 que representa la similaridad entre los mismos basándose en la distancia euclídea. Para esto elimina las valoraciones que no hayan realizado ambos usuarios y calcula la similaridad basándose en el resto.

### `remove_non_common_scores`

Esta función recibe dos vectores de valores flotantes que representan las valoraciones de dos usuarios y devuelve los dos vectores tras eliminar todas las valoraciones que no hayan sido realizadas por ambos usuarios.

### predictions

Este fichero contiene las funciones encargadas del cálculo de la predicciones de las valoraciones de los usuarios:

#### `simple_prediction`

Esta función recibe el vector similarity, que almacena para cada vecino, su indice, su similitud con u y el valor del item en la posicion incognita, y ademas recibe el número de vecinos a considerar, devuelve la predicción de la valoración del usuario utilizando la predicción simple, redondeada a tres decimales.

#### `difference_with_average`

Esta función recibe el vector similarity, que almacena para cada vecino, su indice, su similitud con u y el valor del item en la posicion incognita, y ademas recibe el número de vecinos a considerar, la matrix de utilidad para calcular las medias y el indice del vector u a resolver la incognita, devuelve la predicción de la valoración del usuario utilizando la diferencia con la media, redondeada a tres decimales.

### main

Este fichero contiene el cuerpo principal del programa. En este se recogen los argumentos pasados por consola por el usuario, se lee el fichero que contiene los datos de la matriz, se despejan las incógnitas en base a las opciones escogidas y se muestran por pantalla los resultados de cada uno de los cálculos y la matriz final al completo.

## Ejemplo de uso

Un ejemplo de uso sería el siguiente: `python3 src/main.py -f example.txt -v 3 -m 1 -p 1`

Llamamos al intérprete *python3* con el fichero a ejecutar *src/main.py* y añadimos las opciones para la ejecución:
* -f | --filename: Nombre del fichero de entrada con la matriz de utilidad
* -v | --nVecinos: Número de vecinos a considerar
* -m | --metrica: Métrica elegida - 1. Correlación de Pearson. 2. Distancia coseno. 3. Distancia euclídea.
* -p | --prediccion: Tipo de predicción elegida - 1. Predicción simple. 2. Diferencia con la media.
