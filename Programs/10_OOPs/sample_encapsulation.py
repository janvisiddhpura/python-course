# encapsulation = data binding
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        # private variable using __ (double underscores)
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal")

    def get_balance(self):
        return self.__balance

acc1 = BankAccount("Oggy", 900000)
print("Initial", acc1.get_balance())
acc1.deposit(5000)
print("After deposit", acc1.get_balance())
acc1.withdraw(2000)
print("After withdraw", acc1.get_balance())

# now, this variable will not be accessible
# acc1.balance = 1000000
# print(acc1.name, acc1.__balance)