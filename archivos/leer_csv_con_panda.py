import pandas as pd

#Usando la funcion read_csv apra leer archivo CSV
df = pd.read_csv("archivos\\Prueba.csv")
df2 = pd.read_csv("archivos\\Prueba.csv")

#Obteniendo los datos de la columna nombre
nombres = df["nombre"]


#Ordenando el dataframe por la edad
df_ordenado_ascendente = df.sort_values("edad")

#Ordenando de forma descendente 
df_ordenado_descendente = df.sort_values("edad", ascending=False)

#concatenando los 2 dataframe
df_concatenando = pd.concat([df,df2])

#acediendo a la primera 3 fila con head()
primer_fila = df.head(3)

#acediendo a la ultima 3 fila con tail()
ultima_fila = df.tail(3)

#acediendo  a la cantidad de filas y columnas con shape
# fila_columnas_totales = df.shape
# fila_totales = fila_columnas_totales[0]
# columans_totales = fila_columnas_totales[1]
# filas_totales, columnas_totales = df.shape


#Obteniendo data estadistica del dataframe con describe():
df_info = df.describe()


# accediendo a la edad de la fila 2 con iloc
elemento_especifico_iloc = df.iloc[2, 2] 


# accediendo a la edad de la fila 2
elemento_especifico_loc = df.loc[2, "edad"] 


#accediendo a toda la fila de una columna
apellidos = df.iloc[:, 1]


# accediendo con la fila 3 con loc
fila_3 = df.loc[2,:]


# accediendo a la filas con edad mayor que 30
mayor_que_30 = df.loc[df["edad"]<30,:]
print(mayor_que_30)

