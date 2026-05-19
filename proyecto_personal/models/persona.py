from utils.archivo import guardar_en_txt

class Persona:
    def __init__(self, nombres, apellidos, cedula, edad, direccion):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.edad = edad
        self.direccion = direccion
        
    def mostrar_info(self):
        print("\n--- DATOS DE PERSONA ---")
        print(f"Nombres: {self.nombres}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Cédula: {self.cedula}")
        print(f"Edad: {self.edad}")
        print(f"Dirección: {self.direccion}")
        
    def convertir_a_texto(self):
        return f"{self.nombres}, {self.apellidos}, {self.cedula}, {self.edad}, {self.direccion}"
    
    def guardar(self):
        guardar_en_txt("data/personas.txt", self.convertir_a_texto())