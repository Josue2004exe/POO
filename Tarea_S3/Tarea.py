# Implementa en Python las siguientes clases:
# Clase Persona con atributos (minimo 10).
# Clase Estudiante que herede de Persona y agregue 5 atributos propios.
# Clase Profesor que herede de Persona y agregue 5 atributos propios.
# Implementa métodos propios (mínimo 3) en cada clase para mostrar información.
# Aplica polimorfismo: crea una función presentarse() que se comporte diferente según si es un Estudiante o un Profesor (usar los datos personales del estudiante (nombres, edad, etc)).
class Persona:
    def __init__(self, cedula, nombre, apellido, edad, genero, direccion , telefono, correo, fecha_nacimiento, nacionalidad):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad
        
    def mostrar_datos_personales(self):
        print("======MOSTRANDO DATOS PERSONALES=========")
        print(f"Cedula: {self.cedula}")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Genero: {self.genero}")
        
    def mostrar_contacto(self):
        print("======MOSTRANDO CONTACTO======")
        print(f"Direccion: {self.direccion}")
        print(f"Telefono: {self.telefono}")
        print(f"Correo: {self.correo}")
    
    def mostrando_informacion_general(self):
        print("========MOSTRANDO INFORMACION GENERAL=======")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}")
        print(f"Nacionalidad: {self.nacionalidad}")
        
        
class Estudiante(Persona):
    def __init__(self, cedula, nombre, apellido, edad, genero, direccion , telefono, correo, fecha_nacimiento, nacionalidad, matricula, carrera, semestre, promedio, jornada):
        super().__init__(cedula, nombre, apellido, edad, genero, direccion , telefono, correo, fecha_nacimiento, nacionalidad)
        
        self.matricula = matricula
        self.carrera = carrera
        self.semestre = semestre
        self.promedio = promedio
        self.jornada = jornada
        
    def mostrar_datos_estudiante(self):
        print("======MOSTRANDO DATOS ESTUDIANTE=========")
        print(f"Matricula: {self.matricula}")
        print(f"Carrera: {self.carrera}")
        print(f"Semestre: {self.semestre}")
        
        
    def mostrar_rendimiento_academico(self):
        print("======MOSTRANDO RENDIMIENTO ACADEMICO======")
        print(f"Promedio: {self.promedio}")
        print(f"Jornada: {self.jornada}")
        
    
    def presentarse(self):
        print(f"Hola soy {self.nombre} {self.apellido}, tengo {self.edad} años, "f"Soy estudiante de {self.carrera} y estoy en {self.semestre}.")
        
class Profesor(Persona):
    def __init__(self, cedula, nombre, apellido, edad, genero, direccion , telefono, correo, fecha_nacimiento, nacionalidad, 
                codigo_profesor, especialidad, materia, anio_experiencia, titulo_academico):
        super().__init__(cedula, nombre, apellido, edad, genero, direccion , telefono, correo, fecha_nacimiento, nacionalidad)
        
        self.codigo_profesor = codigo_profesor
        self.especialidad = especialidad
        self.materia = materia
        self.anio_experiencia = anio_experiencia
        self.titulo_academico = titulo_academico
        
    def mostrar_datos_profesor(self):
        print("======MOSTRANDO DATOS PROFESOR=========")
        print(f"Codigo del profesor: {self.codigo_profesor}")
        print(f"Especialidad: {self.especialidad}")
        print(f"Titulo academico: {self.titulo_academico}")
        
        
    def mostrar_materia(self):
        print("======MOSTRANDO INFORMACION DE MATERIA======")
        print(f"Materia que enseña: {self.materia}")
        print(f"Años de experiencia: {self.anio_experiencia}")
        
    
    def presentarse(self):
        print(f"Hola soy profesor {self.nombre} {self.apellido}, tengo {self.edad} años, "f"Soy especialista en {self.especialidad} y enseño {self.materia}.")

# Polimorfismo
def presentarse(persona):
    persona.presentarse()
    
    
est1 = Estudiante(
    "096545646650", "Luis", "Martinez", 20,
    "Masculino", "Guayaquil", "0993871273981",
    "alexpc77@gmail.com", "10/06/2004", "Ecuatoriano", 
    "EST01", "Desarrollo de software", "4to semestre", 9.1,
    "Matutina"
)

prof1= Profesor(
    "0965464565464","Flavio", "Morales", 42,
    "Masculino", "Guayaquil", "09938714545",
    "alexpc77@gmail.com", "10/06/1994", "Ecuatoriano",
    "PROF01","Programacion", "Programacion orientada objeto", 12,
    "Ingeniero en sistema"
)

print("===========INFORMACION DEL ESTUDIANTE=======")
est1.mostrar_datos_personales()
est1.mostrar_contacto()
est1.mostrar_datos_estudiante()
est1.mostrar_rendimiento_academico()
est1.mostrando_informacion_general()
presentarse(est1)



print("===========INFORMACION DEL PROFESOR=======")
prof1.mostrar_datos_personales()
prof1.mostrar_contacto()
prof1.mostrar_datos_profesor
prof1.mostrar_materia()
prof1.mostrando_informacion_general()
presentarse(prof1)