# from tkinter import *
# window= Tk()
# window.title("TITLE")
# window.configure(bg='cyan')
# window.minsize(200,200)
# window.maxsize(500,500)
# window.geometry("400x400+0+0")

# txt1=Label(window,text="Hello world",font=("Arial",50),fg="red",bg="yellow")
# txt1.grid(column=1,row=1)

# window.mainloop()



from tkinter import *

root = Tk()  # create a root widget

root.title("Simple Calculator")

root.configure(bg="light Green",
               cursor="spider", ###   arrow  cross   dot circle  plus
               highlightcolor="red", 
               highlightthickness=4)

root.minsize(500, 700)  
root.maxsize(500, 700)
root.geometry("500x700+50+50")  # width x height + x + y

global s
s = ''
# global pre
# pre=' '
def press(x):
    x1=x
    global s
    s=s.lstrip('0')

    f=[' + ',' - ',' * ',' / ']
    for i in f:
        s=s.lstrip(i) 

    zz=[" + "," - "," * "," / "]
    if x in zz:
        for j in zz:
            if s[-3:]==j:
                s=s[:-3]
 
    s = s + str(x)
    
    number.set(s)
   


def clr():
    global s
    s = ''
    en.delete(0, END)

def bck():
    global s
    s = s[:-1]
    en.delete(0, END)
    en.insert(END, s)

def cal():
    if s[-4:]==' / 0':
        number.set("zero")
        number.set("Can't Divide by Zero")
    else:    
        result=eval(s)
        en.delete(0, END)
        en.insert(END, result)



number=StringVar()

en = Entry(root,
           textvariable=number,
            bg='white',
            justify='left',
		    font=('calibre',14,'normal'))
en.grid(row=0,columnspan=4,column=0,
         ipadx=80,ipady=25,
         sticky="nsew",
         padx=15, pady=10)

b1 =Button(root, text="1", 
               font=("Arial", 16), 
               fg="black",
               bg="white",
               command=lambda: press(1),
               height=4,width=8)
b2 =Button(root, text="2", 
               font=("Arial", 16), 
               fg="black", 
               bg="white",
               command=lambda: press(2),
               height=4,width=8)
b3 =Button(root, text="3", 
               font=("Arial", 16), 
               fg="black", 
               bg="white",
               command=lambda: press(3),
               height=4,width=8)
bplus=Button(root, text="+", 
               font=("Arial", 16), 
               fg="black", 
               bg="white",
               command=lambda: press(" + "),
               height=4,width=8)
b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)
bplus.grid(row=1,column=3)



b4 =Button(root, text="4", 
               font=("Arial", 16), 
               fg="black", 
               bg="white",
               command=lambda: press(4),
               height=4,width=8)
b5 =Button(root, text="5", 
               font=("Arial", 16), 
               fg="black", 
               bg="white",
               command=lambda: press(5),
               height=4,width=8)
b6 =Button(root, text="6", 
               font=("Arial", 16), 
               fg="black", 
               bg="white",
               command=lambda: press(6),
               height=4,width=8)
bmin =Button(root, text="-", 
               font=("Arial", 16), 
               fg="black", 
               bg="white",
               command=lambda: press(" - "),
               height=4,width=8)
b4.grid(row=2,column=0,padx=8, pady=6)
b5.grid(row=2,column=1,padx=8, pady=6)
b6.grid(row=2,column=2,padx=8, pady=6)
bmin.grid(row=2,column=3,padx=8, pady=6)




b7 =Button(root, text="7", 
               font=("Arial", 16), 
               fg="black", 
               bg="white",
               command=lambda: press(7),
               height=4,width=8)
b8 =Button(root, text="8", 
               font=("Arial", 16), 
               fg="black", 
               bg="white",
               command=lambda: press(8),
               height=4,width=8)
b9 =Button(root, text="9", 
               font=("Arial", 16), 
               fg="black", 
               bg="white",
               command=lambda: press(9),
               height=4,width=8)
bmul =Button(root, text="*", 
               font=("Arial", 16), 
               fg="black", 
               bg="white",
               command=lambda: press(" * "),
               height=4,width=8)
b7.grid(row=3,column=0,padx=8, pady=6)
b8.grid(row=3,column=1,padx=8, pady=6)
b9.grid(row=3,column=2,padx=8, pady=6)
bmul.grid(row=3,column=3,padx=8, pady=6)






b0 =Button(root, text="0", 
               font=("Arial", 16), 
               fg="black", 
               bg="white",
               command=lambda: press('0'),
               height=4,width=8)
bop =Button(root, text="(", 
               font=("Arial", 16), 
               fg="black", 
               bg="white",
               command=lambda: press('('),
               height=4,width=8)
bcl =Button(root, text=")", 
               font=("Arial", 16), 
               fg="black", 
               bg="white",
               command=lambda: press(')'),
               height=4,width=8)
bdot =Button(root, text=".", 
               font=("Arial", 16), 
               fg="black", 
               bg="white",
               command=lambda: press('.'),
               height=4,width=8)

b0.grid(row=4,column=0,padx=8, pady=6)
bop.grid(row=4,column=1,padx=8, pady=6)
bcl.grid(row=4,column=2,padx=8, pady=6)
bdot.grid(row=4,column=3,padx=8, pady=6)



clr =Button(root, text="CLR", 
               font=("Arial", 16), 
               fg="black", 
               bg="blue",
               command=clr,
               height=4,width=8)
back =Button(root, text="<--", 
               font=("Arial", 16), 
               fg="black", 
               bg="white",
               command=bck,
               height=4,width=8)
eq =Button(root, text="=", 
               font=("Arial", 16), 
               fg="black", 
               bg="Red",
               command=cal,
               height=4,width=8)
bdiv =Button(root, text="/", 
               font=("Arial", 16), 
               fg="black", 
               bg="white",
               command=lambda: press(" / "),
               height=4,width=8)
clr.grid(row=5,column=0,padx=8, pady=6)
back.grid(row=5,column=1,padx=8, pady=6)
eq.grid(row=5,column=2,padx=8, pady=6)
bdiv.grid(row=5,column=3,padx=8, pady=6)






root.mainloop()    