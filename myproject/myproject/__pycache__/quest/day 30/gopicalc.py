from tkinter import *
from tkinter.ttk import *
w=Tk()
o=['/','-','*','+','%']
p=["/","*","%"]
def zero_check():
    a=t.get()
    if a=='0':
        clear()

xx='+','-'
def pp():
    zero_check()
    a=t.get()
    if a[2] in xx and a[3]=='%' :
        b=eval(a)
        t.delete(END)
        t.insert(b)


def clear():
    t.delete(0,END)
def back():
    a=t.get()
    l=len(a)
    t.delete(l-1)
def neg():
    a=t.get()
    a=int(a)
    a=-a
    clear()
    t.insert(END,a)
def div():
    a=t.get()
    if len(a)>1:
        c=a[len(a)-1]
        if c in o:
            t.delete(len(a)-1,END)
            t.insert(END,'/')
        else:
            t.insert(END,'/')

    else:
        t.insert(END,'/')
def sev():
    zero_check()
    t.insert(END,'7')
def eig():
    zero_check()
    t.insert(END,'8')
def nine():
    zero_check()
    t.insert(END,'9')
def mult():
    a=t.get()
    if len(a)>1:
        c=a[len(a)-1]
        if c in o:
            t.delete(len(a)-1,END)
            t.insert(END,'*')
        else:
            t.insert(END,'*')

    else:
        t.insert(END,'*')
def four():
    zero_check()
    t.insert(END,'4')
def five():
    zero_check()
    t.insert(END,'5')
def six():
    zero_check()
    t.insert(END,'6')
def sub():
    a=t.get()
    if len(a)>1:
        c=a[len(a)-1]
        if c in o:
            t.delete(len(a)-1,END)
            t.insert(END,'-')
        else:
            t.insert(END,'-')



    else:
        t.insert(END,'-')
def one():
    zero_check()
    t.insert(END,'1')
def two():
    zero_check()
    t.insert(END,'2')
def three():
    zero_check()
    t.insert(END,'3')
def add():
    a=t.get()
    if len(a)>1:
        c=a[len(a)-1]
        if c in o:
            t.delete(len(a)-1,END)
            t.insert(END,'+')
        else:
            t.insert(END,'+')

    else:
        t.insert(END,'+')
def mod():
    t.insert(END,'%')
def zero():
    zero_check()
    t.insert(END,'0')
def dot():
    t.insert(END,'.')
def ans():
    
    
    
    a=t.get()
    clear()
    if a in o:
        t.insert(END,"Error")
    elif a[len(a)-1] in o:
        t.insert(END,a)
        
        if a[len(a)-1]!='%':
            
            t.delete(len(a)-1,END)
        else:
            t.delete(len(a)-1,END)
            b=t.get()
            clear()
            t.insert(END,int(b)/100)
            
    elif len(a)==2:
        if a[0] in p:
            t.insert(END,"Error")
        else:
            t.insert(END,a[1])
    else:
        b=eval(a)
        t.insert(END,b)






t=Entry(w)
b1=Button(w,text="clear",command=clear)
b2=Button(w,text="<-",command=back)
b3=Button(w,text="+/-",command=neg)
b4=Button(w,text="/",command=div)
b5=Button(w,text="7",command=sev)
b6=Button(w,text="8",command=eig)
b7=Button(w,text="9",command=nine)
b8=Button(w,text="x",command=mult)
b9=Button(w,text="4",command=four)
b10=Button(w,text="5",command=five)
b11=Button(w,text="6",command=six)
b12=Button(w,text="-",command=sub)
b13=Button(w,text="1",command=one)
b14=Button(w,text="2",command=two)
b15=Button(w,text="3",command=three)
b16=Button(w,text="+",command=add)
b17=Button(w,text="%",command=mod)
b18=Button(w,text="0",command=zero)
b19=Button(w,text=".",command=dot)
b20=Button(w,text="=",command=ans)
b21=Button(w,text="$",command=pp)


t.grid(row=0,column=0,columnspan=3)
b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)
b4.grid(row=1,column=3)
b5.grid(row=2,column=0)
b6.grid(row=2,column=1)
b7.grid(row=2,column=2)
b8.grid(row=2,column=3)
b9.grid(row=3,column=0)
b10.grid(row=3,column=1)
b11.grid(row=3,column=2)
b12.grid(row=3,column=3)
b13.grid(row=4,column=0)
b14.grid(row=4,column=1)
b15.grid(row=4,column=2)
b16.grid(row=4,column=3)
b17.grid(row=5,column=0)
b18.grid(row=5,column=1)
b19.grid(row=5,column=2)
b20.grid(row=5,column=3)
b21.grid(row=10,column=10)



w.mainloop()