class User:		# aqui está lo que tenemos hasta ahora
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # agrega el método deposit

    def __str__(self):
        return self.name + self.email

    def make_deposit(self, amount):  # toma un argumento que es el monto del depósito
        # la cuenta del usuario específico aumenta por la cantidad del valor recibido
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        #self.account_balance < amount:
        #print(f"No tiene Saldo suficiente, el saldo actual es: {self.account_balance} Falta: {amount - self.account_balance}")
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        return f"Usuario: {self.name}, Saldo: {self.account_balance}"

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.make_deposit(amount)


guido = User("Guido van Rossum", "guido@python.com")
guido.make_deposit(350)
guido.make_deposit(300)
guido.make_deposit(500)
guido.make_withdrawal(530)

# print(guido)

monty = User("Monty Python", "monty@python.com")
monty.make_deposit(650)
monty.make_deposit(1000)
monty.make_withdrawal(400)
monty.make_withdrawal(100)
# print(monty)

ely = User("Elizabeth Hernandez", "elizabeth.hernandezc@gmail.com")
ely.make_deposit(3500)
ely.make_withdrawal(500)
ely.make_withdrawal(1000)
ely.make_withdrawal(1000)
ely.transfer_money(guido, 500)
# print(ely)
# print(guido.name)	# salida: Guido van Rossum
# print(monty.name)	# salida: Monty Python


print(guido.display_user_balance())
print(monty.display_user_balance())
print(ely.display_user_balance())


# print(guido.account_balance)	# salida: 300
# print(monty.account_balance)	# salida: 50
