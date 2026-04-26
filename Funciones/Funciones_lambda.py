numeros = [1,2,3,4,5,6,7,8,9]

# creando una funcion lambda pra multiplicar por * 2 
# multiplicar_por_dos = lambda x : x*2  

# creando funcion comun que diga si es par o no 
# def es_par(num):
#     if(num%2 == 1):
#         return True

# #usando filtre con una funcion comun 
# numeros_pares = filter(es_par, numeros)


# creando lo mismo que ante pero con lambda
numeros_pares = filter(lambda numero:numero%2 == 0, numeros)
print(list(numeros_pares))