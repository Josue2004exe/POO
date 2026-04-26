# creando la lista 
frutas = ["guineo","manzana", "pera", "uva", "kiwi"]
cadena = "Hola mundo"
numeros = [2,4,5,6,7]
# evitando que se cioma una fruta con la sentencia [continue]  
# for fruta in frutas:
#     if fruta == 'pera':
#         continue
#     print(f"Me voy a comer estas frutas: {fruta}")
    
    
# evitar que el bucle siga ejecutandose (el else no se ejecuta tampoco porque esta el break)
for fruta in frutas:
    print(f"Me voy a comer una {fruta}")
    if fruta == "uva":
        break
else:    
    print("Saliendo del bucle.....")
    
    
# recorrer una cadena de texto
for letra in cadena:
    print (letra)



# num_duplicado = list()
# for numero in numeros:
#     num_duplicado.append(numero*2)

# print(num_duplicado)



# for en una sola linea de codigo (duplicamos los numeros)
num_duplicado = [x*2 for x in numeros]
print(num_duplicado)



