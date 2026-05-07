from abc import ABC, abstractclassmethod
# INTERFAZ
class Pago(ABC):
    
    # Metodos de interfaz no tienen logica
    @abstractclassmethod
    def procesar_pago(self, monto):
        pass
    
    @abstractclassmethod
    def validar(self):
        pass
        
class TarjetaCredito(Pago):
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        
    def procesar_pago(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            print("Pago realizado con tarjeta")
        else:
            print("Fondo insuficiente POBRE SAL DEL PAIS CHAMO")

    def validar(self):
        print("El pago ha sido validado correctamente.....")
        
# tj1 = TarjetaCredito("12463216381732187", "Fernando el castroso", 100)
# tj1.procesar_pago(660)
    

class TransferenciBancaria(Pago):
    def __init__(self, cuenta, titular, saldo):
        self.cuenta = cuenta
        self.titular = titular
        self.saldo = saldo
        
    def procesar_pago(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            print("Pago realizado con exito su transferencia...")
        else:
            print("Fondo insuficiente Pobre")
            
    def validar(self):
        print("El pago ha sido validado correctamente.....")
        
tj2 = TransferenciBancaria("00399100992", "Fernando Soto", 200)
tj2.procesar_pago(2200)

        