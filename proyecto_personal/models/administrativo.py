from models.colaborador import Colaborador
from utils.archivo import guardar_en_txt

class Administrativo(Colaborador):
    def __init__(
        self,
        nombres,
        apellidos,
        cedula,
        edad,
        direccion,
        codigo_empleado,
        correo_institucional,
        area_trabajo,
        fecha_ingreso,
        sueldo,
        departamento,
        cargo,
        horario,
        extension_telefonica,
        tipo_contrato
):
        super().__init__(
            nombres,
            apellidos,
            cedula,
            edad,
            direccion,
            codigo_empleado,
            correo_institucional,
            area_trabajo,
            fecha_ingreso,
            sueldo
            
        )
        self.departamento = departamento
        self.cargo = cargo
        self.horario = horario
        self.extension_telefonica = extension_telefonica
        self.tipo_contrato = tipo_contrato
    
    def mostrar_info(self):
        print("\n--- DATOS DE ADMINISTRATIVO ---")
        super().mostrar_info()
        print(f"Departamento: {self.departamento}")
        print(f"Cargo: {self.cargo}")
        print(f"Horario: {self.horario}")
        print(f"Extensión telefónica: {self.extension_telefonica}")
        print(f"Tipo de contrato: {self.tipo_contrato}")
        
        
    def convertir_a_texto(self):
        datos_colaborador = super().convertir_a_texto()
        return f"{datos_colaborador},{self.departamento},{self.cargo},{self.horario},{self.extension_telefonica},{self.tipo_contrato}"
    
    def guardar(self):
        guardar_en_txt("data/administrativos.txt", self.convertir_a_texto())

