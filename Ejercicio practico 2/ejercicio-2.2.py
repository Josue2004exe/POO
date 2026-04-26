# creando una funcion que nos devuelva los numeros primos
# entre 0 y el argumento que pasamos

# crear una funcion que verifique si un numero es primo 
def es_primos(num): 
    # verificamos que el numero pasado no pueda dividirse
    # por ningun numero entre 2 y ese mismo -1
    for i in range(2,num-1):
        # si es divisible por alguno  retornamos false y termina el bucle
        if num%i==0: return False
    # si termina el bucle, significaa que no fue divisible entonces es primo 
    return True

# creando funcion que retorne una lista con todos los primos
def primo_hasta(num):
    # creamos la lista
    primos = []
    for i in range (3,num+1):
        # verificamos si el valor es primo 
        resultado = es_primos(i)
        # en caso de que sea lo agregamos a la lista
        if resultado == True: primos.append(i)
        
    # devolvemos la lista 
    return primos
# creamos el resultado llamando a la funcion y lo mostramos 
resultado = primo_hasta(999)
print(resultado)
        