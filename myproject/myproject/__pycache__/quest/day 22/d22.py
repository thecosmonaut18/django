# class Father():
#     def __init__(self,fname):
#         print("i am father",fname)
#     def fa_walking(self):
#         print("Father can walk")

# class Mother():
#     def __init__(self,mname):
#         print("I am mother",mname)
#     def mo_walking(self):
#         print("Mother can Walk")

# class Child(Mother,Father):
#     def __init__(self,cname):
#         print("I am Child",cname)
#         Father.__init__(self,"Raja")
#         Mother("Rani")
#     def ch_walking(self):
#         print("Child can walk")

# Sneha=Child('Sneha')
# Sneha.ch_walking()
# Sneha.fa_walking()
# Sneha.mo_walking()







# class Shopping_cart():
#     def __init__(self):
#         self.cart={}
#     def adding(self,n,p):
#         self.cart[n]=p
#     def delete(self,n):
#         del self.cart[n]

#     def total(self):
#         print("Total=",sum(self.cart.values()))

#     def display(self):
#         print(self.cart)


# customer1=Shopping_cart()
# customer1.adding("phone",12000)
# customer1.adding("earphone",2000)
# customer1.adding("iphone",72000)
# customer1.adding("case",700)
# customer1.total()
# customer1.display()
# print("////delete////")
# customer1.delete("iphone")
# customer1.total()
# customer1.display()
# print("//// CUSTOMER 2 ////")
# customer2=Shopping_cart()
# customer2.adding("phone",13700)
# customer2.adding("case",750)
# customer2.adding("charger",500)
# customer2.total()
# customer2.display()