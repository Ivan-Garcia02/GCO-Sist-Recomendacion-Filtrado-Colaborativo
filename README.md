# Sistemas de recomendación. Métodos de filtrado colaborativo

### Iván García González

### Daniel Jorge Acosta

## Instrucciones de instalación

Python

## Descripción del código

El código del proyecto se encuentra en dividido en varios ficheros.

### file_reader

Contiene la función `read_file`, encargada de crear un array de dos dimensiones a partir del contenido del fichero de entrada. Además, controla que los valores de este array se encuentren entre el mínimo y el máximo establecidos en el fichero y que todas sus filas tengan la misma longitud. La matriz devuelta tendrá sustituidas las incógnitas por el valor -1.0 y sus valores se modificarán para que se sitúen en el intervalo [0.0, max - min], en lugar de [min, max], con el objetivo de facilitar el trabajo con esta.

## Ejemplo de uso
