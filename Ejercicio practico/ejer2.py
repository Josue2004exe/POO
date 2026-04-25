# le pedimos al usuario que nos diga una frase(o varias)
frase = input("Decirme un frase y te calculo cuanto tardarias si tuvieras que decirlas: ")

# creamos una lista con todas las palabras de la frase (separan cada ves que haya un espacio en blanco)
palabras_separadas = frase.split(" ")

# usamos len() para ver la cantidad de elementos que hay en la lista
cantidad_de_palabras = len(palabras_separadas)

# en caso de que tarde mas de un minuto en decirlo le decimos que pare un poco 
if cantidad_de_palabras > 120:
    print("--------------")
    print("Para flaco tomate un cafe mejor")

# calculamos cuanto tardaria en decir las palabras y se lo decimos 
print("---------------")
print(f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundo en decirlo')
print("----------------")
print(f'Dalto lo diria en {cantidad_de_palabras * 100 // 2 *1.3 /100} segundos')

