# class A:
#     def a1(self):
#         print("A1 ")
#     def a2(self):
#         print("A2")

# class B(A):
#     def b1(self):
#         print("B1")
#     def a2(self):
#         print("Modifies b2")


# V=B()
# V.a2()


from abc import ABC , abstractmethod


# class Polygon(ABC):
#     @abstractmethod
#     def no_of_sides(self):
#         pass
#     def show(self):
#         print("Show")

# class Square(Polygon):
#     def no_of_sides(self):
#         print("Four")
#     def Area(self,a):
#         print(a*a)

# class Rectangle(Polygon):
#     def no_of_sides(self):
#         print("Four")
#     def Area(self,l,b):
#         print(l*b)

# v=Rectangle()
# v.Area(2,5)


# class Calc(ABC):
#     @abstractmethod
#     def add(self):
#         pass
#     @abstractmethod
#     def sub(self):
#         pass
#     @abstractmethod
#     def mul(self):
#         pass
#     @abstractmethod
#     def div(self):
#         pass
#     def default(self):
#         print("Wrong input")

# class Calculator(Calc):
#     def add(self,a,b):
#         print("sum = ",a+b)
#     def sub(self,a,b):
#         print("Diff =",a-b)
#     def mul(self,a,b):
#         print("Mul =",a*b)
#     def div(self,a,b):
#         print("Div =",a/b)

# v=Calculator()
# v.add(2,8)
# v.div(8,2)
# v.sub(8,2)
# v.mul(2,8)



