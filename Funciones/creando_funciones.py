# creando una funcion simple

# def saludar():
#     print("A Fernando le gusta la gorditas")
    
# # Ejecutando la funcion simple
# saludar()

def saludar(nombre, sexo):
    # print(f"Hola {nombre}, como estas bro todo bien")
    sexo = sexo.lower()
    if (sexo == "homoxesual"):
        adjetivo = "Princesa"
    elif (sexo == "Hombre"):
        adjetivo = "Macho alfa"
    else:
        adjetivo = "Duda"
    print(f"Hola {nombre}, como estas {adjetivo} todo bien")

# saludar("Caldito de pollo", "Homoxesual")


# crear una funcion que nos retorne multiples valores
def creando_contraseña_random(num):
    chars = "abcdefghij"
    num_entero =  str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num

# desempaquetando la funcion  
password, primer_numero  = creando_contraseña_random(13231)

# Mostrando los resultados obtenido y los datos utilizados para obtenerlos 
print(f"Tu contraseña nueva es: {password}")
print(f"El numero utilizado para crearla fue: {primer_numero}")