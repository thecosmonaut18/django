from tkinter import *
from tkinter.ttk import *
window=Tk()
window.title("Calculator")
window.geometry("400x400")
p=["+","-","*","/"]
q=['/','*']
number=StringVar()
txt1=Entry(window,textvariable=number,font=("Arial",20),width=15)
default=0
txt1.insert(0,default)
txt1.grid(column=0,columnspan=4,row=0)


def zerocheck():
    a=txt1.get()
    if a=='0':
        txt1.delete(0,END)
        # CE()
    #     pass
    elif len(a)>1 and   a[-2] in p and a[-1]=='0':
        txt1.delete(len(a)-1)
# xx='+','-'
# def pp():
#     zerocheck()
#     a=txt1.get()
#     if a[2] in xx and a[3]=='%' :
#         b=eval(a)
#         txt1.delete(END)
#         txt1.insert(b)


def One():
    zerocheck()
    # a=txt1.get()
    # a.lstrip(0)
    txt1.insert(END,"1")

def Two():
    zerocheck()
    txt1.insert(END,"2")
def Three():
    zerocheck()
    txt1.insert(END,"3")
def Four():
    zerocheck()
    txt1.insert(END,"4")
def Five():
    zerocheck()
    txt1.insert(END,"5")
def six():
    zerocheck()
    txt1.insert(END,"6")
def seven():
    zerocheck()
    txt1.insert(END,"7")
def Eight():
    zerocheck()
    txt1.insert(END,"8")
def nine():
    zerocheck()
    txt1.insert(END,"9")
def zero():
    zerocheck()
    txt1.insert(END,"0")
def plus():
    pp()
    a=txt1.get()
    if a[-1] in p:
        txt1.delete(len(a)-1,END)
        txt1.insert(END,'+')
    else:
        txt1.insert(END,'+')
def sub():
    pp()
    a=txt1.get()

    if a[-1] in p:
        txt1.delete(len(a)-1,END)
        txt1.insert(END,'-')
    else:
        txt1.insert(END,'-')

def mul():

    a=txt1.get()

    if a[-1] in p:
        txt1.delete(len(a)-1,END)
        txt1.insert(END,'*')
    else:
        txt1.insert(END,'*')
    # txt1.insert(END,"*")
def div():
    a=txt1.get()

    if a[-1] in p:
        txt1.delete(len(a)-1,END)
        txt1.insert(END,'/')
    else:
            txt1.insert(END,'/')
    # txt1.insert(END,"/")
def equal():
    
    x=txt1.get()
    # CE()
    if x in p:
        txt1.insert(END,"ERROR")
    elif x[len(x)-1] in p:
        txt1.insert(END,x)
    elif len(x)==2:
        if x[1] in q:
            txt1.insert(END,"ERROR")
        else:
            txt1.insert(END,x[1])
    else:


        y=(eval (x))
        txt1.delete(0,END)
        txt1.insert(END,y)
def CE():
    txt1.delete(0,END)
    # default=0
    txt1.insert(0,'0')
    
def back():
    a=len(txt1.get())
    if a==0:

        txt1.delete(a-1,END)
    else:
    
        default=0
        txt1.insert(0,default)
Bt1=Button(window,text="1",command=One)
Bt1.grid(column=1,row=1)

Bt2=Button(window,text="2",command=Two)
Bt2.grid(column=2,row=1)

Bt3=Button(window,text="3",command=Three)
Bt3.grid(column=3,row=1)

Bt4=Button(window,text="4",command=Four)
Bt4.grid(column=1,row=2)

Bt5=Button(window,text="5",command=Five)
Bt5.grid(column=2,row=2)

Bt6=Button(window,text="6",command=six)
Bt6.grid(column=3,row=2)

Bt7=Button(window,text="7",command=seven)
Bt7.grid(column=1,row=3)

Bt8=Button(window,text="8",command=Eight)
Bt8.grid(column=2,row=3)

Bt9=Button(window,text="9",command=nine)
Bt9.grid(column=3,row=3)

Bt0=Button(window,text="0",command=zero)
Bt0.grid(column=2,row=4)

Bte=Button(window,text="=",command=equal)
Bte.grid(column=1,row=4)

Btp=Button(window,text="+",command=plus)
Btp.grid(column=3,row=4)

Bts=Button(window,text="-",command=sub)
Bts.grid(column=4,row=1)

Btd=Button(window,text="/",command=div)
Btd.grid(column=4,row=2)

Btm=Button(window,text="*",command=mul)
Btm.grid(column=4,row=3)

BtB=Button(window,text="<=",command=back)
BtB.grid(column=4,row=4)

BtCE=Button(window,text="CE",command=CE)
BtCE.grid(column=4,row=0)







window.mainloop()