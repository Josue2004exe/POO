#Cambiar el tipo de dato de una columna 
import pandas as pd
df = pd.read_csv("Resolviendo_problemas\\Prueba.csv")

#Convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str)


#Mostrar el tipo de dato del primer elemento de la columna edad
# print(type(df['edad'][0]))

#Remplazando los datos "Flavio" por Crack
df['apellido'].replace("Flavio", "Crack" )



#Eliminando las filas con datos vacios
df = df.dropna()
# print(df)

#Eliminando las filas repetidas
df = df.drop_duplicates()

#Creando un CSV con el dataframe  resultante(lImpio)
df.to_csv("Resolviendo_problemas\\Prueba_limpias.csv")
print(df)