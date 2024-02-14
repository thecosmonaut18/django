#-------------------------#without object Label

# from tkinter import *

# a=Tk()
# a.title('Welcome')
# a.geometry('400x400')
# a.maxsize(900,900)
# a.minsize(250,250)



# Label(a,text="hai welcome to qis").grid(row=0,column=0)

# Entry().grid(row=0,column=1)


# a.mainloop()



#-------------------------#disabled

# from tkinter import *

# a=Tk()
# a.title('Welcome')
# a.geometry('400x400')
# a.maxsize(900,900)
# a.minsize(250,250)



# lb1=Label(a,text="  a:    ")
# lb1.grid(row=0,column=0)

# txt1=Entry(a,state=DISABLED)
# txt1.grid(row=0,column=1)

# lb2=Label(a,text="  b:    ")
# lb2.grid(row=1,column=0)

# txt2=Entry()
# txt2.grid(row=1,column=1)


# a.mainloop()



#-------------------------#focus()

# from tkinter import *

# a=Tk()
# a.title('Welcome')
# a.geometry('400x400')
# a.maxsize(900,900)
# a.minsize(250,250)



# lb1=Label(a,text="  a:    ")
# lb1.grid(row=0,column=0)

# txt1=Entry()
# txt1.grid(row=0,column=1)
# txt1.focus()

# lb2=Label(a,text="  b:    ")
# lb2.grid(row=1,column=0)

# txt2=Entry()
# txt2.grid(row=1,column=1)


# a.mainloop()



#-------------------------#delete()

# from tkinter import *

# a=Tk()
# a.title('Welcome')
# a.geometry('400x400')
# a.maxsize(900,900)
# a.minsize(250,250)



# lb1=Label(a,text="  a:    ")
# lb1.grid(row=0,column=0)

# txt1=Entry()
# txt1.grid(row=0,column=1)

# lb2=Label(a,text="  b:    ")
# lb2.grid(row=1,column=0)

# txt2=Entry()
# txt2.grid(row=1,column=1)

# def click():
#     # txt1.delete(2,4)
#     # txt1.delete(2)
#     # txt1.delete(-1)
#     # txt1.delete(END)
#     txt1.delete(0,END)
    

# bt1=Button(a,text="Click me",command=click)
# bt1.grid(row=2,column=1)

# a.mainloop()



#-------------------------#ttk module

# from tkinter import *
# from tkinter.ttk import *

# a=Tk()
# a.title('Welcome')
# a.geometry('400x400')
# a.maxsize(900,900)
# a.minsize(250,250)



# lb1=Label(a,text="  a:    ")
# lb1.grid(row=0,column=0)
# txt1=Entry()
# txt1.grid(row=0,column=1)

# lb2=Label(a,text="  b:    ")
# lb2.grid(row=1,column=0)
# txt2=Entry()
# txt2.grid(row=1,column=1)


# bt1=Button(a,text="Click me")
# bt1.grid(row=2,column=1)


# a.mainloop()



#-------------------------#combo box and current()

# from tkinter import *
# from tkinter.ttk import *

# a=Tk()
# a.title('Welcome')
# a.geometry('400x400')


# c=Combobox(a)
# c['values']=(1,2,3,4,5)
# c.grid()

# c.current(0)        #giving name to combo box using inside elemets using index positions

# a.mainloop()



# -------------------------#combo box accessing values

# from tkinter import *
# from tkinter.ttk import *

# a=Tk()
# a.title('Welcome')
# a.geometry('400x400')


# c=Combobox(a)
# c['values']=(1,2,3,4,5)
# c.grid()

# c.current(0)        

# def chkcmbo():
#     a=c.get()
#     print(a)

# btnc=Button(a,text="click me", command=chkcmbo)
# btnc.grid()

# a.mainloop()



#-------------------------#checkbox

# from tkinter import *
# from tkinter.ttk import *

# a=Tk()
# a.title('Welcome')
# a.geometry('400x400')

# chkbt=Checkbutton(a,text='choose')
# chkbt.grid(row=0,column=0)


# a.mainloop()



#-------------------------#checkbox with accessing 3 states

# from tkinter import *
# from tkinter.ttk import *

# a=Tk()
# a.title('Welcome')
# a.geometry('400x400')

# chkbt=Checkbutton(a,text='choose')
# chkbt.grid(row=0,column=0)


# def chkbtn():
#     a=chkbt.state()
#     print(a)


# btn1=Button(a,text='click me',command=chkbtn)
# btn1.grid()



# a.mainloop()



#-------------------------#checkbox with accessing 2 states using BooleanVar()
#---------------#true or false

# from tkinter import *
# from tkinter.ttk import *

# a=Tk()
# a.title('Welcome')
# a.geometry('400x400')

# chk1=BooleanVar()
# chk1.set(False)

# chk2=Checkbutton(a,text='choose',var=chk1)
# chk2.grid(row=0,column=0)



# def chkbtn():
#     a=chk2.state()
#     print(a)

#     d=chk2.instate(['selected'])
#     print(d)


# btn1=Button(a,text='click me',command=chkbtn)
# btn1.grid()



# a.mainloop()




#-------------------------#checkbox with accessing 2 states using BooleanVar() 
#---------------# 1 or 0

# from tkinter import *
# from tkinter.ttk import *

# a=Tk()
# a.title('Welcome')
# a.geometry('400x400')

# chk1=IntVar()
# chk1.set(1)

# chk2=Checkbutton(a,text='choose',var=chk1)
# chk2.grid(row=0,column=0)



# def chkbtn():
#     a=chk2.state()
#     print(a)

#     d=chk2.instate(['selected'])
#     print(d)


# btn1=Button(a,text='click me',command=chkbtn)
# btn1.grid()



# a.mainloop()