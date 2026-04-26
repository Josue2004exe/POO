# # Forma  optima para sumar valores 
# def suma_total(numeros):
#     return sum([*numeros])

# resultado2 = suma_total([4,5,7])
# print(resultado2)


# utilizando el parametro args * como argumento 
def suma(nombre,*numeros):
    return f"{nombre}, la suma de tus numeros es:  {sum(numeros)}"
    
resultado = suma("Flavio", 4,5,7)
print(resultado)



