#----------------------------#GRAPHICAL USER INTERFACE

#---------------------#from tkinter importing * and tk() and mainloop()

# from tkinter import *
# a=Tk()
# a.mainloop()



#---------------------#title()

# from tkinter import *

# a=Tk()
# a.title('Welcome to GUI')

# a.mainloop()



#---------------------#grid()  label() 

# from tkinter import *

# a=Tk()
# a.title('Welcome to GUI')


# lb1=Label(a,text="hai welcome to qis")
# lb1.grid(row=10,column=10)

# a.mainloop()



#---------------------#geometry() minsize() maxsize()

# from tkinter import *

# a=Tk()
# a.title('Welcome to GUI')
# a.geometry('500x500')
# a.maxsize(900,900)
# a.minsize(250,250)

# # Label(a,text="hai").grid(row=11,column=11)

# lb1=Label(a,text="hai welcome to qis")
# lb1.grid(row=10,column=10)

# lb2=Label(a,text="hello world!!")
# lb2.grid(row=0,column=0)

# lb3=Label(a,text="python")
# lb3.grid(row=3,column=3)

# lb4=Label(a,text="python")
# lb4.grid(row=4,column=4)

# a.mainloop()



# ---------------------#Entry()

# from tkinter import *

# a=Tk()
# a.title('Welcome to GUI')
# a.geometry('500x500')
# a.maxsize(900,900)
# a.minsize(250,250)

# lb1=Label(a,text="Enter your name:")
# lb1.grid()
# txt1=Entry()
# # #txt1.grid()
# txt1.grid(row=0,column=1)

# lb2=Label(a,text="Enter your age:")
# lb2.grid()
# txt2=Entry()
# txt2.grid(row=1,column=1)

# a.mainloop()


#---------------------#BUTTON()

# from tkinter import *

# a=Tk()
# a.title('Welcome to GUI')
# a.geometry('500x500')
# a.maxsize(900,900)
# a.minsize(250,250)


# lb1=Label(a,text="Enter your name:")
# lb1.grid()
# txt1=Entry()
# txt1.grid(row=0,column=1)


# lb2=Label(a,text="Enter your age:")
# lb2.grid()
# txt2=Entry()
# txt2.grid(row=1,column=1)


# bt1=Button(a,text='SUBMIT')
# bt1.grid()

# a.mainloop()



#---------------------#BUTTON() with function using command button and get method

# from tkinter import *

# a=Tk()
# a.title('Welcome to GUI')
# a.geometry('500x500')
# a.maxsize(900,900)
# a.minsize(250,250)


# lb1=Label(a,text="Enter your name:")
# lb1.grid()
# txt1=Entry()
# txt1.grid(row=0,column=1)


# lb2=Label(a,text="Enter your age:")
# lb2.grid()
# txt2=Entry()
# txt2.grid(row=1,column=1)


# # def myvalue():
# #     print("haii")

# def myvalue():
#     name=txt1.get()       #get()
#     age=txt2.get()
#     print(name)
#     print(age)


# bt1=Button(a,text='SUBMIT',command=myvalue)
# bt1.grid()

# a.mainloop()



#---------------------#configure()

from tkinter import *

a=Tk()
a.title('Welcome to GUI')
a.geometry('500x500')
a.maxsize(900,900)
a.minsize(250,250)


lb1=Label(a,text="Enter your name:")
lb1.grid(row=0,column=0)
txt1=Entry()
txt1.grid(row=0,column=1)


lb2=Label(a,text="Enter your age:")
lb2.grid(row=1,column=0)
txt2=Entry()
txt2.grid(row=1,column=1)


lb3=Label(a,text="what is your name?")
# lb3=Label(a,text="what is your name and age?")
lb3.grid()


def myvalue():
    name=txt1.get()
    # age=txt2.get()
    # print(name)
    # print(age)

    lb3.configure(text="my name is "+name)
    # lb3.configure(text="my name is "+name+" and My age is "+age)


bt1=Button(a,text='SUBMIT',command=myvalue)
bt1.grid()

a.mainloop()