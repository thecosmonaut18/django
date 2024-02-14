# class A:
#     def __init__(self) :
#         print("A init")
#     def show(self):
#         print("A show")
# class B(A):
#     def __init__(self):
#         print("B init")
#         # A.__init__()            #error no fn bracket()
#         # A.__init__(self)
#         # A().__init__()
          # A()
#         super().__init__()
#         super().show()

# anu=B()



# class Myage:
#     age=21

# class Myobj(Myage):
#     name="Jilson"
#     age=21


# # x=issubclass(Myobj,Myage)
# x=issubclass(Myage,Myobj)
# print(x)


# class A:
#     def __init__(self) :
#         print("A init")
#     def show(self):
#         print("A show")

# Obj=A()
# x=isinstance(Obj,A)
# print(x)


# class Vehicle:
#     def __init__(self,brand,model,year):
#         self.brand=brand
#         self.model=model
#         self.year=year

# class Car(Vehicle):
#     def __init__(self,num_door, brand, model, year):
#         self.num_door=num_door
#         super().__init__(brand, model, year)
#         print("CAR")
#     def display(self):
#         print("Number of Door =",self.num_door)
#         print("Brand =",self.brand)
#         print("Model =",self.model)
#         print("Year =",self.year)

# class Bike(Vehicle):
#     def __init__(self,num_whl, brand, model, year):
#         self.num_whl=num_whl
#         super().__init__(brand, model, year)
#         print("BIKE")
#     def display(self):
#         print("Number of Wheel =",self.num_whl)
#         print("Brand =",self.brand)
#         print("Model =",self.model)
#         print("Year =",self.year)


# Ducati=Bike(2,"Ducati","Panigale V4",2021)
# Ducati.display()
# Koingesegg=Car(4,"Koingesegg","Gamera",2023)
# Koingesegg.display()



class Bank_acc:
    def __init__(self,accno,bal) :
        self.accno=accno
        self.bal=bal

    def Withdraw(self,amount):
        self.amount=amount
        print("Balance =",self.bal-self.amount)

class Savings_acc(Bank_acc):
    pass
    # def __init__(self):
    #     print("Balance =",self.bal)

    # def Withdraw(self,amount):
    #     self.amount=amount
    #     print("Balance =",self.bal-self.amount)

class Checking_acc(Bank_acc):
    # pass
    # def __init__(self):
    #     print("Balance =",self.bal)

    def Withdraw(self,amount):
        self.amount=amount
        if self.amount<=500:
            print("Transaction Successful")
            self.bal=self.bal-self.amount
            print("Balance =",self.bal)
        else:
            print("Withdraw limit Exeeded")


john=Checking_acc(123,50000)
john.Withdraw(500)
# john=Checking_acc(123,50000)
john.Withdraw(500)
# john=Checking_acc(123,50000)
john.Withdraw(400)

Cosmo=Savings_acc(1234,10000000000)
Cosmo.Withdraw(4208718)
        
