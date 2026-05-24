class MiExcepcion(Exception):
    #Creando mi propia excepcion
    def __init__(self,err):
        print(f"Impresionante, cometiste un error: {err}")
#Lanzando mi propia excepcion
# raise MiExcepcion("jajaja como cometiste ese error")

#Manejandola
try:
    raise MiExcepcion("jajaja como cometiste ese error")
except:
    print("So tremendo pobre")
        
