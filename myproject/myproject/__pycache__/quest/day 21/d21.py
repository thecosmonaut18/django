# class Human:
#     eyes=2
#     legs=2
#     def walking(self):
#         print("can walk")
#     def talking(self):
#         print("can talk")


# anu=Human()
# anu.walking()
# anu.talking()




# class Human:
#     eyes=2
#     legs=2
#     def walking(k,m):
#         k.g=m
#         print("can walk",m)
#     def talking(kk):
#         print("can talk",kk.g)


# anu=Human()
# anu.walking(99)
# anu.talking()



# class Human:
#     eyes=2
#     legs=2
#     def __init__(self):
#         print("i am human")
#     def walking(self):
#         print("can walk")
#     def talking(self):
#         print("can talk")

# anu=Human()     #init always calls in initialisation


class Human:
    eyes=2
    legs=2
    def __init__(self,name):
        self.fname=name
        print("i am human. My name is ",name)
    def walking(self):
        print(self.fname,"can walk")
    def talking(self):
        print(self.fname,"can talk")

anu=Human("Anu")
ravi=Human("Ravi")
anu.talking()
ravi.walking()



# class Rectangle:
#     def __init__(self,length,breadth):
#         self.rlength=length
#         self.rbreadth=breadth
#         print("length=",length)
#         print("breadth=",breadth)

#     def area(self):
#         print("Area= ",self.rlength*self.rbreadth)


# rect=Rectangle(2,4)
# rect.area()


class Student:
     def __init__(self,name,rollno,grade=[]):
          self.sname=name
          self.srno=rollno
          self.sgrade=grade
          print("Name =",name)
          print("Roll no =",rollno)
          print("Grade",grade)
     # def grade(self):
          

# raju=Student("Raju",18,77,88)