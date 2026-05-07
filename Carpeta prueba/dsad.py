class programacion():
    def __init__(self, nombre, lenguaje):
        self.nombre = nombre
        self.lenguaje = lenguaje

    def mostrar(self):
        print(f"El programa {self.nombre} está escrito en {self.lenguaje}.")