from models.persona import Persona
from utils.archivo import guardar_en_txt

class Colaborador(Persona):
    def __init__(
        self, nombres, 
        apellidos, 
        cedula, 
        edad,
        direccion,
        codigo_empleado,
        correo_institucional,
        area_trabajo,
        fecha_ingreso,
        sueldo
    ):
        super().__init__(nombres, apellidos, cedula, edad, direccion)
        self.codigo_empleado = codigo_empleado
        self.correo_institucional = correo_institucional
        self.area_trabajo = area_trabajo
        self.fecha_ingreso = fecha_ingreso
        self.sueldo = sueldo
        
    def mostrar_info(self):
        print("\n--- DATOS DE COLABORADOR ---")
        super().mostrar_info()
        print(f"Codigo Empleado: {self.codigo_empleado}")
        print(f"Correo institucional: {self.correo_institucional}")
        print(f"Area de trabajo: {self.area_trabajo}")
        print(f"Fecha de ingreso: {self.fecha_ingreso}")
        print(f"Sueldo $: {self.sueldo}")
    
    def convertir_a_texto(self):
        datos_persona = super().convertir_a_texto()
        return f"{datos_persona}, {self.codigo_empleado}, {self.correo_institucional}, {self.area_trabajo}, {self.fecha_ingreso}, {self.sueldo}"
        
    def guardar(self):
        guardar_en_txt("data/colaboradores.txt", self.convertir_a_texto())