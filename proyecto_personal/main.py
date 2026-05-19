from models.persona import Persona
from models.colaborador import Colaborador
from models.docente import Docente
from models.administrativo import Administrativo
from utils.archivo import leer_txt

def pedir_datos_persona():
    print("\n--- INGRESO DE DATOS PERSONALES ---")
    nombres = input("Ingrese su nombre: ")
    apellidos = input("Ingrese su apellidos: ")
    cedula = input("Ingrese cedula: ")
    edad = input("Ingrese edad: ")
    direccion = input("Ingrese su direccion: ")
    return nombres, apellidos, cedula, edad, direccion

def perdir_datos_colaborador():
    print("\n--- INGRESO DE DATOS DE COLABORADOR ---")
    codigo_empleado = input("Ingrese el codigo del empleado: ")
    correo_institucional = input("Ingrese correo institucional: ")
    area_trabajo = input("Ingrese area de trabajo: ")
    fecha_ingreso = input("Ingrese fecha de ingreso: ")
    sueldo = input("Ingrese sueldo: ")
    
    return codigo_empleado, correo_institucional, area_trabajo, fecha_ingreso, sueldo


def registrar_persona():
    datos_persona = pedir_datos_persona()
    persona = Persona(*datos_persona)
    persona.mostrar_info()
    persona.guardar()
    print("\nPersona guardada correctamente.")
    
def registrar_colaborador():
    datos_persona = pedir_datos_persona()
    datos_colaborador = perdir_datos_colaborador()
    
    colaborador = Colaborador(*datos_persona, *datos_colaborador)
    colaborador.mostrar_info()
    colaborador.guardar()
    print("\nColaborador guardado correctamente.")
    
def registrar_docente():
    datos_persona = pedir_datos_persona()
    datos_colaborador = perdir_datos_colaborador()
    
    print("\n--- INGRESO DE DATOS DE DOCENTE ---")
    facultad = input("Ingrese facultad: ")
    asignatura = input("Ingrese asignatura: ")
    nivel_academico = input("Ingrese nivel académico: ")
    horas_clase = input("Ingrese horas de clase: ")
    modalidad = input("Ingrese modalidad: ")
    
    docente = Docente(
        *datos_persona,
        *datos_colaborador,
        facultad,
        asignatura,
        nivel_academico,
        horas_clase,
        modalidad
    )
    
    docente.mostrar_info()
    docente.guardar()
    print("\nDocente guardado correctamente.")
    
    
def registrar_administrativo():
    datos_persona = pedir_datos_persona()
    datos_colaborador = perdir_datos_colaborador()
    print("\n--- INGRESO DE DATOS DE ADMINISTRATIVO ---")
    departamento = input("Ingrese departamento: ")
    cargo = input("Ingrese cargo: ")
    horario = input("Ingrese horario: ")
    extension_telefonica = input("Ingrese extensión telefónica: ")
    tipo_contrato = input("Ingrese tipo de contrato: ")
    
    
    administrativo = Administrativo(
        *datos_persona,
        *datos_colaborador,
    departamento,
    cargo,
    horario,
    extension_telefonica,
    tipo_contrato

    )
    administrativo.mostrar_info()
    administrativo.guardar()
    print("\nAdministrativo guardado correctamente.")
    
    
def mostrar_registros():
    print("\n========== REGISTROS GUARDADOS ==========")
    print("\n--- PERSONAS ---")
    for linea in leer_txt("data/personas.txt"):
        print(linea.strip())

    print("\n--- COLABORADORES ---")
    for linea in leer_txt("data/colaboradores.txt"):
        print(linea.strip())
    print("\n--- DOCENTES ---")
    for linea in leer_txt("data/docentes.txt"):
        print(linea.strip())
    print("\n--- ADMINISTRATIVOS ---")
    for linea in leer_txt("data/administrativos.txt"):
        print(linea.strip())
        
            
def menu():
    opcion = ""
    
    while opcion != "6":
        print("\n SISTEMA DE REGISTRO INSTITUCIONAL ")
        print("1. Registrar persona")
        print("2. Registrar colaborador")
        print("3. Registrar docente")
        print("4. Registrar administrativo")
        print("5. Mostrar registros")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_persona()
        elif opcion == "2":
            registrar_colaborador()
        elif opcion == "3":
            registrar_docente()
        elif opcion == "4":
            registrar_administrativo()
        elif opcion == "5":
            mostrar_registros()
        elif opcion == "6":
            print("Saliendo del sistema...")
        else:
            print("Opción incorrecta. Intente nuevamente.")      
menu()