import csv

with open("archivos\\Prueba.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)