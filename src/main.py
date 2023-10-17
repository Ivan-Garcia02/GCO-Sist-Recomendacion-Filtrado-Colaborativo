import argparse
import numpy
import math
import sys
from file_reader import read_file

def pearson(u_values, v_values):
    sum = 0
    div_u = 0
    div_v = 0

    for i in range(len(u_values)):
        u_sum, v_sum, number_of_values = 0, 0, 0

        for j in range(len(u_values)):
            if u_values[j] >= 0 and v_values[j] >= 0:
                u_sum += u_values[j]
                v_sum += v_values[j]
                number_of_values += 1
        u_average = u_sum / number_of_values
        v_average = v_sum / number_of_values

        if u_values[i] >= 0 and v_values[i] >= 0:
            sum += (u_values[i] - u_average) * (v_values[i] - v_average)
            div_u += math.pow((u_values[i] - u_average), 2)
            div_v += math.pow((v_values[i] - v_average), 2)

    return round(sum / (math.sqrt(div_u) * math.sqrt(div_v)), 10)

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
                print(similarity[i][0] + 1)


#x = args.foo
#print(x)
#print(parser.parse_args(sys.argv[1:]))
