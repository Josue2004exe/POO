import re
texto = '''Hola maestro 1 esta es la primera linea de parrafo. como esta mi capitan
esta es la segunda linea de 222 parrafo. para ver el rendimiento de esta propiedad
y esta es la final crack'''

#haciendo una busqueda simple
# resultado = re.findall("esta", texto, flags=re.IGNORECASE)

#d\ -> busca digitos numericos del 0 - 9
# resultado = re.findall(r"\d", texto)

#w\ -> busca caracter alfa numerico del [a-z A-Z 0-9 _]
# resultado = re.findall(r"\w", texto)

#w\ -> busca TODO menos caracter alfa numerico del [a-z A-Z 0-9 _]
# resultado = re.findall(r"\W", texto)

#d\ -> busca TODO Menos digitos numericos del 0 - 9
# resultado = re.findall(r"\D", texto)

#s\ -> busca espacios en blanco -> espacios, tab, saltos dee line
# resultado = re.findall(r"\s", texto)

#S\ -> busca TODO menos espacios en blanco -> espacios, tab, saltos dee line
# resultado = re.findall(r"\S", texto)

# . ->busca TODO menos salto en linea
# resultado = re.findall(f".", texto)

# \n -> busca saltos en linea
# resultado = re.findall(r'\n',texto)


# \ -> cancelar careacter especiale, cancelando la funcion del punto y buscando puntos
# resultado = re.findall(r"\.", texto)


#armando una cadena que busque un numero, seguido de un punto y un epacio
# resultado = re.findall(f'\d\.\s', texto)

#Buscando el principio de una linea 
#ˆ->busca el comienzo de una lina (Buscando Hola al principio de una linea)
#flags=re.M activa la multilinea
# resultado = re.findall(f'^esta', texto, flags=re.M)

#$ ->busca el Final de una lina 
# resultado = re.findall(f'crack$', texto, flags=re.M)

# {n} -> busca n cantidad de veces el valor de la izquierda
# resultado = re.findall(r'\d{3}', texto)

# {n,m} -> al menos n, como maximo m
# resultado = re.findall(r'\d{1,4}', texto)

#| -> busca una cosa o la otra
resultado = re.findall(r'\d{1,4}|Hola', texto)

print(resultado)

