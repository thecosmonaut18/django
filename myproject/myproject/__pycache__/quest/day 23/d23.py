# class Stack():
#     def __init__(self):
#         self.stack=[]
#     def adding(self,n):
#         self.stack.append(n)
#     def de(self,n):
#         self.stack.remove(n)
#     def display(self):
#         print(self.stack)

# stck1=Stack()
# stck1.adding(123)
# stck1.adding(456)
# stck1.adding(789)
# stck1.adding(321)
# stck1.display()
# print("///DELETE///")
# stck1.de(321)
# stck1.display()
# print("///STACK 2///")
# stck2=Stack()
# stck2.adding(777)
# stck2.adding(222)
# stck2.adding(666)
# stck2.adding(111)
# stck2.display()
# print("///DELETE///")
# stck2.de(222)
# stck2.display()




# class Student():
#     Name="Swathi"
#     age=21
#     course="BCA"

# # swathi=Student()
# # delattr(Student,'age')
# swathi=Student()
# # print(swathi)
# # x=getattr(swathi,'Name')
# # print(x)
# # x=hasattr(swathi,"course")
# # print(x)
# setattr(swathi,'Sec_Name','Krishna')
# # print(swathi.Sec)
# x=getattr(swathi,'Sec_Name')
# print(x)




class Student:
    school="K V"
    def __init__(self,name,id,age) :
        self.name=name
        self.id=id
        self.age=age
    def display(self):
        print(self.name,self.id,self.age)


Stud1=Student("Jilson",101,21)
Stud2=Student("Swathi",102,21)
Stud1.display()
Stud2.display()


