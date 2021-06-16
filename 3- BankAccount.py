class Banco:
    def __init__(self,tasa_int, saldo=0):
        self.tasa_int = tasa_int
        self.saldo = saldo

    def deposito(self, monto):
        self.saldo += monto
        return self

    def retiro(self, monto):
        self.saldo -= monto
        return self

    def MostrarSaldo(self):
        return self.saldo
    
    def AumentaInteres(self):
        if self.saldo > 0 :
            self.saldo= self.saldo * (1 + self.tasa_int)
            return self.saldo
    def MuestraInteres(self):
        return (f"{1 + self.tasa_int}%")


cuenta1 = Banco(0.02,1000)
cuenta2 = Banco(0.03)

cuenta1.deposito(500).deposito(2000).retiro(300)
cuenta2.deposito(1500).deposito(5000).retiro(1800).retiro(100).retiro(800).retiro(500)

print("El Saldo inicial de la cuenta es de:",cuenta1.MostrarSaldo(), ", la tasa de Interes es de: " , cuenta1.MuestraInteres(),", El saldo con Intereses es de:", cuenta1.AumentaInteres())
print("El Saldo inicial de la cuenta es de:",cuenta2.MostrarSaldo(), ", la tasa de Interes es de: " , cuenta2.MuestraInteres(),", El saldo con Intereses es de:", cuenta2.AumentaInteres())