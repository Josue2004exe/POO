class ServicioCorreo:
    def enviar_correo(self, destinatario, mensaje, sistema ):
        print(f"{sistema} - Enviando correo a {destinatario}: {mensaje}")
        
    def validar_conexion(self):
        return True

class SistemaAcademico:
    def __init__(self, nombre, version, institucion):
        self.nombre = nombre
        self.version = version
        self.institucion = institucion
        
    
    def enviar_notificacion(self, correo, mensaje):
        servicio = ServicioCorreo()#Dependencia
        if servicio.validar_conexion():
            servicio.enviar_correo(correo, mensaje, self.nombre)
        else:
            print("No se valido correctamente la conexion ")
        
sistema = SistemaAcademico("SGA", "1.0", "Unemi")
sistema.enviar_notificacion("alexpc77@gmial.com", "Mensaje automatico")