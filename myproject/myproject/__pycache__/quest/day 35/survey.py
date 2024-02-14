from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext

a=Tk()
a.title('Survey')
a.geometry('500x500')
# a.maxsize(900,900)
# a.minsize(250,250)

Label(a,text='Let us know How we can Improve').place(x=500,y=5)

Label(a,text='Name : ').place(x=500,y=30)
txt1=Entry()
txt1.place(x=550,y=30)

Label(a,text='Email : ').place(x=500,y=55)
txt2=Entry()
txt2.place(x=550,y=55)

Label(a,text='Age : ').place(x=500,y=80)
txt3=Entry()
txt3.place(x=550,y=80)

Label(a,text='Which option best describes your current role?').place(x=290,y=105)


c=Combobox(a)
c['values']=('Student','Teacher','Officer')
c.place(x=550,y=105)
c.current(0)        

l1=Label(a,text="""How likely is that you would recommend this 
                                        program to a friend?""")
l1.place(x=290,y=130)

selected=IntVar()
# selected1=StringVar()
rad1=Radiobutton(a,text="Definitely",variable=selected,value=0)
rad1.place(x=550,y=130)
rad2=Radiobutton(a,text="Maybe",variable=selected,value=1)
rad2.place(x=550,y=155)
rad1=Radiobutton(a,text="Not Sure",variable=selected,value=2)
rad1.place(x=550,y=180)

Label(a,text="What do you like most here?").place(x=380,y=205)

d=Combobox(a)
d["values"]=("Select an option",1,2)
d.current(0)
d.place(x=550,y=205)

a.mainloop()