
class User:
    def __init__(self,name,age):
        print(f"Welcome {name}")
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Your Name is :{self.name}")
        print(f"your age is :{self.age}")


class Bank(User):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.balance = 0

    def deposite(self,amount):
        self.balance += amount
        print(f"Your Current Balance after deposite is {self.balance}")

    def withdraw(self,amount):
        if amount > self.balance:
            print(f"Your Current Balance is {self.balance} so You can`t withdraw :{amount_of_withdraw}")
            return
        self.balance -= amount
        print(f"Your Current Balance after withdraw is {self.balance}")
    
    def show_balance(self):
        print(f"Ur Current Balance is :{self.balance}")



c1=Bank("Mahmoud",22)
c1.deposite(1000)
c1.withdraw(100)
c1.show_details()
c1.show_balance()


