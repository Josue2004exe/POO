animales = ["gato", "perro", "loro", "cocodrilo"]
numeros = [10,20,340,20,2343]

# # recorriendo la lista animales 
# for animal in animales:
#     print(f'ahora la variable animal es igual a: {animal}')
    

# # recorriendo la lista numero cada * 10 
# for numero in numeros: 
#     resultado = numero  * 10
#     print(resultado)
    
    
# iterando  dos lista con la metodo zip()
# for numero, animal in zip(numeros, animales):
#     print(f"recorriendo la lista 1: {numero}")
#     print(f"recorriendo la lista 2: {animal}")




# forma no optima de recorrer una lista 
for num in range(len(numeros)):
    print(numeros[num])
    

# forma correcta de recorrer una lista con su indice usando enumerate()
for num in enumerate(numeros):
    indice = num [0]
    valor = num [1]
    print(f'el indice es: {indice} y el valor es: {valor}')
    
    
# usando el for/else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero} ")
else:
    print("el bucle termino")


# todo lo anterior funciona exactamente igual para tuplas 