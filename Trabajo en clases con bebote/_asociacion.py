class Profesor:
    def __init__(self, nombre, especialidad, experiencia):
        self.nombre= nombre
        self.especialidad = especialidad
        self.experiencia = experiencia
        
    def mostrar_info(self):
        print(f"{self.nombre} - {self.especialidad} - {self.experiencia} años.")


class Estudiante:
    def __init__(self, nombre, edad, carrera, profesor):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.profesor = profesor # Asociacion 
        
        
    def mostrar_info(self):
        print(f"Estudiante: {self.nombre} - Carrera: {self.carrera} - Docente: {self.profesor.nombre} ")
        
        
prof1 = Profesor("Flavio", "Sistema Operativo", 0)

est1 = Estudiante("Fernando", 25, "H4CKER", prof1)
est1 = Estudiante("Freddy", 26, "H4CKER", prof1)
est1 = Estudiante("Martha", 27, "H4CKER", prof1)
est1 = Estudiante("Carlos", 28, "H4CKER", prof1)
est1 = Estudiante("Julio", 29, "H4CKER", prof1)


est1.mostrar_info()

del prof1
est1.mostrar_info()