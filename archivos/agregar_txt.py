with open('archivos\\lectura con .txt','a' ,encoding="UTF-8") as archivo:
    # usando un bucle para agregar varias lineas
    archivo.write("\n")
    for i in range(5):
        # agregando linea 
        archivo.write(f"- Linea {i+1} agregada\n")