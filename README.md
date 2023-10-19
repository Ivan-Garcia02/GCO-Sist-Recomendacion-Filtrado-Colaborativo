# Sistemas de recomendación. Métodos de filtrado colaborativo

### Iván García González

### Daniel Jorge Acosta

## Instrucciones de instalación

Python

## Descripción del código

El código del proyecto se encuentra en dividido en varios ficheros.

### file_reader

Contiene la función `read_file`, encargada de crear un array de dos dimensiones a partir del contenido del fichero de entrada. Además, controla que los valores de este array se encuentren entre el mínimo y el máximo establecidos en el fichero y que todas sus filas tengan la misma longitud. La matriz devuelta tendrá sustituidas las incógnitas por el valor -1.0 y sus valores se modificarán para que se sitúen en el intervalo [0.0, max - min], en lugar de [min, max], con el objetivo de facilitar el trabajo con esta.

### metricas

Contiene las funciones encargadas del cálculo de los grados de similaridad entre usuarios:

#### `pearson`

Esta función recibe dos vectores de valores flotantes que representan las valoraciones de dos usuarios y devuelve un valor entre -1 y 1 que representa la similaridad entre los mismos basándose en el coeficiente de correlación de Pearson. Para esto elimina las valoraciones que no son comunes entre los usuarios y calcula la similaridad basándose en el resto.

#### `cosine_similarity`

Esta función recibe dos vectores de valores flotantes que representan las valoraciones de dos usuarios y devuelve un valor entre -1 y 1 que representa la similaridad entre los mismos basándose en la distancia coseno. Para esto elimina las valoraciones que no son comunes entre los usuarios y calcula la similaridad basándose en el resto.

#### `euclidean_distance`

Esta función recibe dos vectores de valores flotantes que representan las valoraciones de dos usuarios y devuelve un valor entre -1 y 1 que representa la similaridad entre los mismos basándose en la distancia euclídea. Para esto elimina las valoraciones que no son comunes entre los usuarios y calcula la similaridad basándose en el resto.

## Ejemplo de uso
