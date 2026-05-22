with open('archivos\\lectura con .txt','w' ,encoding="UTF-8") as archivo:
    # sobreescribiendo el archivo
    # archivo.write("Fernando es malo en el valorant tiene que mejorar el aim")
    
    # agregando 2 lineas con writelines
    archivo.writelines([" - Su aim es de pobre debe mejorarlo\n", " - Debe mejorar"] )
    
    # agregando otras 2 lineas
    archivo.writelines(["- Su aim es de pobre debe mejorarlo\n", " - Viva Venezuela"] )