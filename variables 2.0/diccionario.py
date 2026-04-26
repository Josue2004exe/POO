# creando diccionario con dict es tambien para crear datos vacios()
diccionario = dict(nombre="flavio" ,apellido= "Morales")

# las listas no puede ser claves y usamos frozenset para meter conjuntos 
diccionario = {frozenset(["FLavio","Molestoso"]):"xd"}


# creando diccionario con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(["nombre", "apellido"])

# creando diccionario con formkeys() cambiando el valor por defecto a nose 
diccionario = dict.fromkeys(["nombre", "apellido"], "no se")



print(diccionario)