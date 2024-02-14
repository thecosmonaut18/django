# class Student:
#     School="K V"
#     def __init__(self,id,name,age) :
#         self.id=id
#         self.age=age
#         self.name=name


# Sara=Student(1,"Sara",10)
# jose=Student(2,"Jose",20)
# # x=getattr(Sara,"name","error")
# # print(x)    
# # setattr(jose,"name","Kris")
# # x=getattr(jose,"name","error")
# # print(x)    
# y=hasattr(Sara,"Place")
# print(y)
# setattr(Student,"Place","Ekm")
# x=getattr(Student,"Place")
# print(x)



class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def get(self):
        x=getattr(self,"name")
        y=getattr(self,'age',"")
        print(x,y)

    def set(self):
        if hasattr(self,"age"):
            setattr(self,"age")
        

John=Person("John",21)
John.get()