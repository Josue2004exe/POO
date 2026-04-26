# creando una funcion de 3 parametros
# ''
# def frase(nombre, apellido, adjetivo):
#     return f'Hola {nombre} {apellido}, sos muy {adjetivo}'

#utilizando keyword argumentos
# frase_resultante = frase(adjetivo="crack",  nombre="Flavio", apellido="Morales")
# print(frase_resultante)



# creando la misma funcion com un parametro opcional y un valor por defecto
def frase(nombre, apellido, adjetivo = "bruto"):
    return f'Hola {nombre} {apellido}, sos muy {adjetivo}'

frase_resultante = frase("Flavio", "Morales", "crack")
print(frase_resultante)
