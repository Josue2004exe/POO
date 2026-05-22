#Usando open para abrir un archivo con una codificacion universal (UTF-8)
archivo = open("archivos\\lectura con .txt", encoding="UTF-8")


# Leer archivo completo 
archivo = archivo.read()


# Leer una sola linea
# linea = archivo.readline() 


# leer linea por linea 
# liena = archivo.readlines()
# print(lienas)


# cerrar el archivo
archivo.close()

print(archivo)