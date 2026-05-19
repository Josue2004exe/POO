from models.colaborador import Colaborador
from utils.archivo import guardar_en_txt


class Docente(Colaborador):
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
        sueldo,
        facultad,
        asignatura,
        nivel_academico,
        horas_clase,
        modalidad
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
        
        self.facultad = facultad
        self.asignatura = asignatura
        self.nivel_academico = nivel_academico
        self.horas_clase = horas_clase
        self.modalidad = modalidad
        
    def convertir_a_texto(self):
        datos_colaborador = super().convertir_a_texto()
        return f"{datos_colaborador}, {self.facultad}, {self.asignatura}, {self.nivel_academico}, {self.horas_clase}, {self.modalidad}"
    
    def guardar(self):
        guardar_en_txt("data/docentes.txt", self.convertir_a_texto())