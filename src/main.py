import argparse
import sys
from file_reader import read_file

parser = argparse.ArgumentParser(prog='ProgramName', description='What the program does', epilog='Text at the bottom of help')
parser.add_argument('-f', '--filename', type=str, required=True, help="Fichero de entrada")
parser.add_argument('-m', '--metrica', type=int, required=True, choices=range(1,4), help="Metrica elegida. 1. Correlacion de Pearson. 2.Distancia coseno. 3.Distancia Euclidea.")
parser.add_argument('-v', '--nVecinos', type=int, required=True, help="Numero de vecinos considerados")
parser.add_argument('-p', '--prediccion', type=int, required=True, choices=range(1,3), help="Tipo de prediccion: 1.Prediccion simple. 2.Diferencia con la media.")

args = parser.parse_args()
read_file(args.filename)
#x = args.foo
#print(x)
#print(parser.parse_args(sys.argv[1:]))
