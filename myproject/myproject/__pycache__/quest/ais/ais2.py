#-------------------------------------#insert()
# from tkinter import *

# a=Tk()
# a.title('Welcome to GUI')
# a.geometry('500x500')
# a.maxsize(900,900)
# a.minsize(250,250)

# lb1=Label(a,text="Enter your name:")
# lb1.grid(row=0,column=0)
# txt1=Entry()
# txt1.grid(row=0,column=1)

# lb2=Label(a,text="Enter your age:")
# lb2.grid(row=1,column=0)
# txt2=Entry()
# txt2.grid(row=1,column=1)


# def name():

#     txt1.insert(0,'ais')

# def age():
#     txt2.insert(0,'21')



# bt1=Button(a,text='name',command=name)
# bt1.grid()

# bt2=Button(a,text='age',command=age)
# bt2.grid()


# a.mainloop()


#---------------------------#insert() with END

# from tkinter import *

# a=Tk()
# a.title('Welcome to GUI')
# a.geometry('500x500')
# a.maxsize(900,900)
# a.minsize(250,250)


# lb1=Label(a,text="Enter your name:")
# lb1.grid(row=0,column=0)
# txt1=Entry()
# txt1.grid(row=0,column=1)


# lb2=Label(a,text="Enter your age:")
# lb2.grid(row=1,column=0)
# txt2=Entry()
# txt2.grid(row=1,column=1)


# def myvalue():
#     print("hai")

# def bt1():
#     # v=txt2.get()
#     # l=len(v)
#     # txt2.insert(l,"1")
#         #or
#     txt2.insert(END,"1")


# def bt2():
#     # v=txt2.get()
#     # l=len(v)
#     # txt2.insert(l,"2")
#         #or
#     txt2.insert(END,"2")
  


# def bt3():
#     # v=txt2.get()
#     # l=len(v)
#     # txt2.insert(l,"3")
#         #or
#     txt2.insert(END,"3")




# bt=Button(a,text='SUBMIT',command=myvalue)
# bt.grid()

# bt1=Button(a,text='1',command=bt1)
# bt1.grid()

# bt2=Button(a,text='2',command=bt2)
# bt2.grid()

# bt3=Button(a,text='3',command=bt3)
# bt3.grid()



# a.mainloop()



#-------------------------#question1

# from tkinter import *

# a=Tk()
# a.title('Welcome')
# a.geometry('500x500')
# a.maxsize(900,900)
# a.minsize(250,250)


# lb1=Label(a,text="Name:")
# lb1.grid()
# txt1=Entry()
# txt1.grid(row=0,column=1)


# lb2=Label(a,text="Email:")
# lb2.grid()
# txt2=Entry()
# txt2.grid(row=1,column=1)


# lb3=Label(a,text="Address:")
# lb3.grid()
# txt3=Entry()
# txt3.grid(row=2,column=1)

# lb4=Label(a)
# lb4.grid(row=4,column=1)
# lb5=Label(a)
# lb5.grid(row=5,column=1)
# lb6=Label(a)
# lb6.grid(row=6,column=1)


# def myvalue():
#     name=txt1.get()
#     email=txt2.get()
#     address=txt3.get()
#     lb4.configure(text="Name: "+name)
#     lb5.configure(text="Email: "+email)
#     lb6.configure(text="Address: "+address)



# bt=Button(a,text='SUBMIT',command=myvalue)
# bt.grid(row=3,column=1)


# a.mainloop()





#-------------------------#question2

# from tkinter import *

# a=Tk()
# a.title('Welcome')
# a.geometry('600x400')
# a.maxsize(900,900)
# a.minsize(250,250)


# lb1=Label(a,text="Num1:")
# lb1.grid(row=0,column=0)
# txt1=Entry()
# txt1.grid(row=0,column=1)


# lb2=Label(a,text="Num2:")
# lb2.grid(row=1,column=0)
# txt2=Entry()
# txt2.grid(row=1,column=1)

# lb3=Label(a,text="Result:")
# lb3.grid(row=3,column=0)
# txt3=Entry()
# txt3.grid(row=3,column=1)

# def add():
#     a=int(txt1.get())
#     b=int(txt2.get())
#     c=a+b
#     txt3.insert(END,c)

# def sub():
#     a=int(txt1.get())
#     b=int(txt2.get())
#     c=a-b
#     txt3.insert(END,c)

# def mul():
#     a=int(txt1.get())
#     b=int(txt2.get())
#     c=a*b
#     txt3.insert(END,c)

# def div():
#     a=int(txt1.get())
#     b=int(txt2.get())
#     c=a/b
#     txt3.insert(END,c)

# bt1=Button(a,text='ADDITION',command=add)
# bt1.grid(row=2,column=0)

# bt2=Button(a,text='SUBTRACTION',command=sub)
# bt2.grid(row=2,column=1)

# bt3=Button(a,text='MULTIPLICATION',command=mul)
# bt3.grid(row=2,column=2)

# bt4=Button(a,text='DIVISION',command=div)
# bt4.grid(row=2,column=3)



# a.mainloop()