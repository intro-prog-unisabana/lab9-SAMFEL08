# utils.py
from bank_account import BankAccount
from person import Person
def person_data():
    name = input("Enter the person's name:\n")
    person = Person(name)
    while True:
        cuenta = int(input("Enter a 4-digit account number:\n"))
        balance = float(input("Enter the initial balance:\n"))
        my_cuenta = BankAccount(cuenta, balance)
        person.add_account(my_cuenta)
        ya = input("Are you done adding accounts? (yes/no):\n").lower()
        if ya == 'yes':
            break
    return person
def balance_summary(person_list):
    for person in person_list:
        total = 0
        for cuentas in person.accounts:
            total += cuentas.balance
        print(f"{person.name} : {total:.2f}")