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
    def muestraInteres(self):
        return (f"{1 + self.tasa_int}%")


class User:		# aqui está lo que tenemos hasta ahora
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account= Banco(tasa_int=0.02, saldo=0)
    # agrega el método deposit

    def __str__(self):
        return self.name + self.email

    def make_deposit(self, amount):  # toma un argumento que es el monto del depósito
        # la cuenta del usuario específico aumenta por la cantidad del valor recibido
        self.account.deposito(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.retiro(amount)
        return self

    def display_user_balance(self):
        return f"Usuario: {self.name}, Saldo: {self.account.saldo}"

    def transfer_money(self, other_user, amount):
        self.account.retiro(amount)
        other_user.make_deposit(amount)
        return self

guido = User("Guido van Rossum", "guido@python.com")
guido.make_deposit(350).make_deposit(300).make_deposit(500).make_withdrawal(530)

#print(guido)

monty = User("Monty Python", "monty@python.com")
monty.make_deposit(650).make_deposit(1000).make_withdrawal(400).make_withdrawal(100)
#print(monty)

ely = User("Elizabeth Hernandez", "elizabeth.hernandezc@gmail.com")
ely.make_deposit(3500).make_withdrawal(500).make_withdrawal(1000).make_withdrawal(1000).transfer_money(guido, 500)
#print(ely)



print(guido.display_user_balance())
print(monty.display_user_balance())
print(ely.display_user_balance())


# print(guido.account_balance)	# salida: 300
# print(monty.account_balance)	# salida: 50

