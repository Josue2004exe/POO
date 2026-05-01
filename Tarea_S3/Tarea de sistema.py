import os  

def gestionar_sistema_archivo():
    nombre_carpeta  = "Tarea_S3"
    nombre_archivo = "datos.txt"
    ruta = os.path.join(nombre_carpeta, nombre_archivo)
    
    if not os.path.exists(nombre_carpeta):
        os.mkdir(nombre_carpeta)
        print(f"'Carpeta '{nombre_carpeta}'creada.'")
    else:
        print("La carpeta ya existe.")
        
    archivo = open (ruta, "w")
    archivo.write("Hola el archivo de prueba esta listo. \n")
    archivo.write("Esto es python basico")
    archivo.close()
    print(f"Archivo' {nombre_archivo} creando y escrito.'")
    
    
    archivo_leer = open(ruta, "r")
    contenido_archivo = archivo_leer.read()
    print("Contenido del archivo: ")
    print(contenido_archivo)
    archivo_leer.close()
    
    os.chmod(ruta, 0o444)
    print(f"Permiso de '{nombre_archivo} cambiados a solo lectura.'")
    
gestionar_sistema_archivo()

    