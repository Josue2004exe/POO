# creando una funcion que suma numeros 
def sumar_dos():
    # iniciando un bucle
    while True: 
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        # intentando convertirlos a enteros y sumarlos
        try: 
            resultado = int(a) + int(b)
        # Si lanzo una excepcion, pedirle que reingrese los datos
        except ValueError as e :
            print("Te pedi un numero pobre no te aga la victima ")
            print(f"ERROR:  {e}")
            
        # Si todo salio bien terminamos el bucle 
        else:
            break
        # finally se ejecuta siempre
        finally:
            print("Manejo de excepcion finalizado....")
    #Si todo salio bien terminamos el bucle
    return resultado

print(sumar_dos())
