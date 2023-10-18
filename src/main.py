import argparse
import numpy
import math
from file_reader import read_file

def pearson(u_values, v_values):
    # Elimina las columnas con incognita
    u_filtered_values = []
    v_filtered_values = []
    for i in range(len(u_values)):
        if u_values[i] >= 0 and v_values[i] >= 0:
            u_filtered_values.append(u_values[i])
            v_filtered_values.append(v_values[i])

    # Calcula el coeficiente de Pearson
    u_average = sum(u_filtered_values) / len(u_filtered_values)
    v_average = sum(v_filtered_values) / len(v_filtered_values)
    numerator = 0
    u_denominator = 0
    v_denominator = 0
    for i in range(len(u_filtered_values)):
        numerator += (u_filtered_values[i] - u_average) * (v_filtered_values[i] - v_average)
        u_denominator += math.pow((u_filtered_values[i] - u_average), 2)
        v_denominator += math.pow((v_filtered_values[i] - v_average), 2)

    return round(numerator / (math.sqrt(u_denominator) * math.sqrt(v_denominator)), 10)

parser = argparse.ArgumentParser(prog='ProgramName', description='What the program does', epilog='Text at the bottom of help')
parser.add_argument('-f', '--filename', type=str, required=True, help="Fichero de entrada")
parser.add_argument('-m', '--metrica', type=int, required=True, choices=range(1,4), help="Metrica elegida. 1. Correlacion de Pearson. 2. Distancia coseno. 3. Distancia Euclidea.")
parser.add_argument('-v', '--nVecinos', type=int, required=True, help="Numero de vecinos considerados")
parser.add_argument('-p', '--prediccion', type=int, required=True, choices=range(1,3), help="Tipo de prediccion: 1. Prediccion simple. 2. Diferencia con la media.")

args = parser.parse_args()
matrix = read_file(args.filename)
if matrix is None:
    print('Ha ocurrido un error leyendo el fichero')
    quit()

print(matrix)

for i in range(len(matrix)):
    for j in matrix[i]:
        if j < 0:
            similarity = []
            for k in range(len(matrix)):
                if i != k:
                    similarity.append((k, pearson(matrix[i], matrix[k])))
            similarity.sort(key=lambda x: x[1], reverse=True)
            print(similarity)

            neighbours = args.nVecinos
            print("Vecinos seleccionados: ")
            for i in range(neighbours):
                print(similarity[i][0])
