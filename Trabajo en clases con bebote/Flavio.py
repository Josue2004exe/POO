# Implementa en Python las siguientes clases:
# Clase Persona con atributos (minimo 10).
# Clase Estudiante que herede de Persona y agregue 5 atributos propios.
# Clase Profesor que herede de Persona y agregue 5 atributos propios.
# Implementa métodos propios (mínimo 3) en cada clase para mostrar información.
# Aplica polimorfismo: crea una función presentarse() que se comporte diferente según si es un Estudiante o un Profesor (usar los datos personales del estudiante (nombres, edad, etc)).
# Explicar la codificación de todo el ejercicio y la ejecución del mismo en un video de máximo 20 minutos, el video debe realizarse sin cortes, sin aumento en la velocidad de reproducción 
# y mostrando el rostro del estudiante mientras explica lo que va realizando, el enlace debe redireccionar al video directamente y debe estar publico. En caso de no cumplirse las especificaciones esta parte de la tarea no ponderará en su calificación. 
class Persona:
    def __init__(self, cedula, nombres, apellidos, edad, genero, direccion, telefono, correo,
                fecha_nacimiento, nacionalidad):
        self.cedula = cedula
        self.nombres = nombres
        self.apellidos = apellidos
        self.edad = edad
        self.genero = genero
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad

    def mostrar_datos_personales(self):
        print("----- DATOS PERSONALES -----")
        print(f"Cédula: {self.cedula}")
        print(f"Nombres: {self.nombres}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Edad: {self.edad}")
        print(f"Género: {self.genero}")

    def mostrar_contacto(self):
        print("\n----- DATOS DE CONTACTO -----")
        print(f"Dirección: {self.direccion}")
        print(f"Teléfono: {self.telefono}")
        print(f"Correo: {self.correo}")

    def presentarse(self):
        print(f"Hola, soy {self.nombres} {self.apellidos}, tengo {self.edad} años y soy una persona.")


class Estudiante(Persona):
    def __init__(self, cedula, nombres, apellidos, edad, genero, direccion, telefono, correo,
                fecha_nacimiento, nacionalidad, matricula, carrera, semestre, promedio, jornada):
        super().__init__(cedula, nombres, apellidos, edad, genero, direccion, telefono, correo,
                        fecha_nacimiento, nacionalidad)

        self.matricula = matricula
        self.carrera = carrera
        self.semestre = semestre
        self.promedio = promedio
        self.jornada = jornada

    def mostrar_datos_estudiante(self):
        print("\n----- DATOS DEL ESTUDIANTE -----")
        print(f"Matrícula: {self.matricula}")
        print(f"Carrera: {self.carrera}")
        print(f"Semestre: {self.semestre}")

    def mostrar_rendimiento(self):
        print("\n----- RENDIMIENTO ACADÉMICO -----")
        print(f"Promedio: {self.promedio}")
        print(f"Jornada: {self.jornada}")

    def presentarse(self):
        print(f"Hola, soy {self.nombres} {self.apellidos}, tengo {self.edad} años, " f"soy estudiante de {self.carrera} y estoy en {self.semestre}.")


class Profesor(Persona):
    def __init__(self, cedula, nombres, apellidos, edad, genero, direccion, telefono, correo,
                fecha_nacimiento, nacionalidad, codigo_profesor, especialidad, materia,
                anios_experiencia, titulo_academico):
        super().__init__(cedula, nombres, apellidos, edad, genero, direccion, telefono, correo,
                        fecha_nacimiento, nacionalidad)

        self.codigo_profesor = codigo_profesor
        self.especialidad = especialidad
        self.materia = materia
        self.anios_experiencia = anios_experiencia
        self.titulo_academico = titulo_academico

    def mostrar_datos_profesor(self):
        print("\n----- DATOS DEL PROFESOR -----")
        print(f"Código de profesor: {self.codigo_profesor}")
        print(f"Especialidad: {self.especialidad}")
        print(f"Título académico: {self.titulo_academico}")

    def mostrar_materia(self):
        print("\n----- INFORMACIÓN DE DOCENCIA -----")
        print(f"Materia que enseña: {self.materia}")
        print(f"Años de experiencia: {self.anios_experiencia}")

    def presentarse(self):
        print(f"Hola, soy el profesor {self.nombres} {self.apellidos}, tengo {self.edad} años, " f"soy especialista en {self.especialidad} y enseño {self.materia}.")


# Función para aplicar polimorfismo
def presentarse(persona):
    persona.presentarse()


# Creación del objeto Estudiante
est1 = Estudiante(
    "1234567890", "Carlos", "Mendoza", 20,
    "Masculino","Quito","0999999999",
    "carlos.mendoza@email.com","10/05/2004","Ecuatoriana", "EST001",
    "Desarrollo de Software","Tercer semestre",9.1,"Matutina"
)


# Creación del objeto Profesor
prof1 = Profesor(
    "0987654321","Luis","Ramírez",42,
    "Masculino","Guayaquil","0988888888",
    "luis.ramirez@email.com","15/03/1982",
    "Ecuatoriana","PROF001","Programación",
    "Programación Orientada a Objetos",12,
    "Ingeniero en Sistemas"
)

# Ejecución del programa
print("\n========== INFORMACIÓN DEL ESTUDIANTE ==========")
est1.mostrar_datos_personales()
est1.mostrar_contacto()
est1.mostrar_datos_estudiante()
est1.mostrar_rendimiento()
presentarse(est1)

print("\n========== INFORMACIÓN DEL PROFESOR ==========")
prof1.mostrar_datos_personales()
prof1.mostrar_contacto()
prof1.mostrar_datos_profesor()
prof1.mostrar_materia()
presentarse(prof1)