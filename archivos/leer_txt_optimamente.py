# Forma optima de abrir un archivo con with open
with open("archivos\\lectura con .txt", encoding="UTF-8") as archivo:
    
    # leemos el archivo
    contenido = archivo.read()
    
    # mostrando el archivo
    print(archivo.read())
    
# no es necesario cerrarlo al usar with open