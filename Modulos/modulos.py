# importando un modulo y asignandole el nombre "saludar"
# import modulo_saludar as saludar_rm

# desde ese modulo, importamos dos funciones y les cambiamos el nombre
from Modulos.modulo_saludar import saludar as saludar_normal, saludar_medio_raro as saludar_como_fer


#Creamos las variables con los resultados 
saludo = saludar_normal("Flavio")
saludar_raro = saludar_como_fer("Fernando")


# Mostramos los resultados
print(saludo)
print( saludar_raro)


# para ver la propiedades y metodos de el namespace
# print(dir(saludar_rm))

# accedemos al nombre de este modulo 
print(__name__)

# accedemos al nombre de este modulo 
print(saludar_normal.__name__)