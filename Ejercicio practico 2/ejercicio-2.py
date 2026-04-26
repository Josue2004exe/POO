# falto el profe y los alumnos van a armar la clase

# pedir el nombre y la edad de los compañeros que vinieron hoy a clase.

def obtener_compañeros(cantidad_de_compañeros):
    # creando la lista con los compañeros
    compañeros = [ ]
    # ejercutando un for para pedir informacion de cada compañero
    for i in range (cantidad_de_compañeros):
        nombre = input("Ingrese  el nombre del compañero: ")
        edad = int(input("Ingrese la edad del compañero: "))
        compañero = (nombre, edad)
        
        # agregando la informacion a la lista
        compañeros.append(compañero)
        
    #ordenandolos de menor a mayor segun la edad 
    compañeros.sort(key=lambda x:x[1])
    
    # compañeros[x] devuelve una tupla con (nombre, edad) y despues accedemos al nombre
    # para pedir al asistente y al profesor 
    asistente = compañeros[0][0]
    profesor = compañeros [-1][0]
    
    #retornamos una tuplas 
    return asistente, profesor

# desempaquetamos lo que nos retorna lafuncion
asistente,profesor = obtener_compañeros(5) 

# mostrando el resultado
print(f"El profesor es: {profesor} y su asistente es {asistente}")