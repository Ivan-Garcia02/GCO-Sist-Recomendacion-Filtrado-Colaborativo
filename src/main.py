import argparse
from file_reader import read_file
from metrics import pearson, cosine_similarity, euclidean_distance
from predictions import simple_prediction, difference_with_average

parser = argparse.ArgumentParser(prog='Métodos de filtrado colaborativo', description='Sistemas de Recomendación')
parser.add_argument('-f', '--filename', type=str, required=True, help="Fichero de entrada")
parser.add_argument('-m', '--metrica', type=int, required=True, choices=range(1,4), help="Metrica elegida. 1. Correlacion de Pearson. 2. Distancia coseno. 3. Distancia Euclidea.")
parser.add_argument('-v', '--nVecinos', type=int, required=True, help="Numero de vecinos considerados")
parser.add_argument('-p', '--prediccion', type=int, required=True, choices=range(1,3), help="Tipo de prediccion: 1. Prediccion simple. 2. Diferencia con la media.")

args = parser.parse_args()
args_read_file = read_file(args.filename)
matrix = args_read_file[0]
min_value = args_read_file[1]
max_value = args_read_file[2]

if matrix is None:
    print('Ha ocurrido un error leyendo el fichero')
    quit()

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] < 0:
            similarity = []
            for k in range(len(matrix)):
                if i != k:
                    if args.metrica == 1:
                        similarity.append((k, pearson(matrix[i][:], matrix[k][:]), matrix[k][j]))
                    elif args.metrica == 2:
                        similarity.append((k, cosine_similarity(matrix[i], matrix[k]), matrix[k][j]))
                    elif args.metrica == 3:
                        similarity.append((k, euclidean_distance(matrix[i], matrix[k]), matrix[k][j]))
                        
            similarity.sort(key=lambda x: x[1], reverse=True)

            # Calculo de la predicción
            neighbours = args.nVecinos
            if args.prediccion == 1:
                matrix[i][j] = simple_prediction(similarity, neighbours)
            elif args.prediccion == 2:
                matrix[i][j] = difference_with_average(similarity, neighbours, matrix, i)
                
            # Impresion de los resultados
            print("\033[1;34mResolvemos la incognita en el vector", i + 1, "\033[0m")
            print("Matrix resultante:")
            for a in range(len(matrix)):
                print("[", end="")
                for b in range(len(matrix[a])):
                    if matrix[a][b] == -1:
                        print(" - ", end=", ")
                    elif a == i and b == j:
                        print("\033[1;33m\b", round((matrix[a][b] + min_value), 3), "\b\033[0m", end=", ")
                    else:
                        print(round((matrix[a][b] + min_value), 3), end=", ")
                print("\b\b]")
            
            print("\nSimilitud entre cada usuario y vecino:")
            for a in range(len(similarity)):
                if a < neighbours:
                    print("\033[1;32msim (", i + 1, ", ", similarity[a][0] + 1, ") = ", similarity[a][1], "\033[0m")
                else:
                    print("sim (", i + 1, ", ", similarity[a][0] + 1, ") = ", similarity[a][1])

            print("Vecinos seleccionados: ", end="")
            for k in range(neighbours):
                print(similarity[k][0] + 1, end=" ")

            print("\n\nPrediccion en base a los vecinos considerados:\033[1;33m", round((matrix[i][j] + min_value), 3), "\033[0m\n\n")
            
# Impresion de la matrix final
print("\033[1;34mMATRIX FINAL:\033[0m")
for i in range(len(matrix)):
    print("[", end="")
    for j in range(len(matrix[i])):
        print(round(matrix[i][j] + min_value, 3), end=", ")
    print("\b\b]")