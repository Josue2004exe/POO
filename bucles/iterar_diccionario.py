diccionario = {
    "nombre:": "Flavio",
    "apellido:":"Morales",
    "seguidores:": 200000
    
}

# recorriendo diccionario para obtener las claves
for key in diccionario:
    key 
    print(f'la clave es: {key}')

#  recorriedo diccionario con items() para obtener la clave y valor 
for datos in diccionario.items():
    key  = datos[0]
    value = datos[1]
    print(f'la clave es: {key} y el valor es: {value}')
    