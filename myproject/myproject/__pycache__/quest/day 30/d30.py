from tkinter import *
window=Tk()
window.title("Welcome")
window.geometry("400x400")
#####   SCROLLED TEXT
from tkinter import scrolledtext
# txt1=scrolledtext.ScrolledText(window,width=10,height=10)
# txt1.grid(column=0,row=10)

# def Scroll():
#     # txt1.insert(1.2,"text")
#     # txt1.delete(1.3)
#     # txt1.delete(1.3,END)
#     print(txt1.get(1.0,END))






# btn1=Button(window,text="Click Here",command= Scroll)
# btn1.grid(column=0,row=11)


####   MESSAGE BOX
from tkinter import messagebox
# def Msg():
#     # messagebox.showinfo("Message","Message BOX")
#     # messagebox.showerror("ERROR","404 ERROR")
#     # messagebox.showwarning("WARNING","WARNING message")


# btn1=Button(window,text="Click Here",command= Msg)
# btn1.grid(column=0,row=11)


#####   PROGRESS BAR
from tkinter.ttk import Progressbar

# bar=Progressbar(window,length=200)
# bar['value']=10
# bar.grid(column=0,row=10)



#####   RADIO BUTTON
from tkinter import *
from tkinter.ttk import *
selected=IntVar()
selected1=StringVar()
rad1=Radiobutton(window,text="First",value="1",variable=selected)
rad2=Radiobutton(window,text='Second',value='2',variable=selected)
rad3=Radiobutton(window,text="English",value='E',variable=selected1)
rad4=Radiobutton(window,text='Malayalam',value='M',variable=selected1)

def click():
    print(selected.get())
    print(selected1.get())

btn=Button(window,text="Clicked radio",command=click)
btn.grid(column=5,row=5)
rad1.grid(column=0,row=1)
rad2.grid(column=1,row=2)
rad3.grid(column=2,row=1)
rad4.grid(column=3,row=2)






window.mainloop()