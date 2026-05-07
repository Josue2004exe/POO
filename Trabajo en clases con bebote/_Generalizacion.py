class Vehiculo :
    # declaramos parametro para alimentar a los atributos de las clases
    def __init__(self, modelo, marca, velocidad_max, combustible):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_max = velocidad_max
        self.combustible = combustible
    
    def consumir_combustible(self, cantidad):
        self.combustible -= cantidad * 0.1
        if self.combustible < 0:
            self.combustible = 0
            print("Sin combustible")
            
    def acelerar(self, incremento):
        if self.combustible > 0: 
            print("El vehiculo puede acelerar")
            self.consumir_combustible(incremento)
        else:
            print("Sin combustible para acelerar")
            
    def mostrar_info(self):
        print(f"Marca: {self.marca} - Modelo: {self.modelo}")
        print("-----------")
        print(f"Velocidad maxima: {self.velocidad_max} km/h")
        print("-----------")
        print(f"Combustible: {round(self.combustible,2)}")
        

# v1 = Vehiculo("Chevorlet", "Captiva", 100, 100)
# v1.mostrar_info()
# clase auto tiene un atributoo propio llamado puertas
class Auto(Vehiculo):
    def __init__(self, modelo, marca, velocidad_max, combustible, puertas):
        super().__init__(modelo, marca, velocidad_max, combustible)
        self.puertas = puertas
    # Polimorfismo
    def acelerar(self, incremento):
        print("El auto va a acelerar")
        super().acelerar(incremento)
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Numero de puertas: {self.puertas}")
        
# a1 = Auto("Chevorlet", "Captiva", 100, 100, 4)
# a1.mostrar_info()
# Clases moto no tiene atributo propios
class Moto(Vehiculo):
    def acelerar(self, incremento):
        print("Moto acelerando")
        super().acelerar(incremento)
    
    def mostrar_info(self):
        print("-------Empresa Moto Morales------")
        super().mostrar_info()

moto1 = Moto("Honda","200p", 150, 100)
moto1.mostrar_info()
#Hasta aqui 