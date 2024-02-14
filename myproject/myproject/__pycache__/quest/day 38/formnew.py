from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import re

form=Tk()
form.title('Form')
form.geometry('500x500')

Label(form,text='Name : ').place(x=500,y=30)
txt1=Entry()
txt1.place(x=650,y=30)

Label(form,text='Phone Number : ').place(x=500,y=55)
txt2=Entry()
txt2.place(x=650,y=55)

Label(form,text='Email : ').place(x=500,y=80)
txt3=Entry()
txt3.place(x=650,y=80)

Label(form,text='Password : ').place(x=500,y=105)
txt4=Entry()
txt4.place(x=650,y=105)

Label(form,text='Confirm Password : ').place(x=500,y=130)
txt5=Entry() 
txt5.place(x=650,y=130)

def submit():

    #     #NAME
    a=txt1.get()
    a1=list(txt1.get())

    a2=re.findall("[a-zA-Z\s]",a)
    if a1==a2:
        print(a)
        
    else:
        txt1.delete(0,END)
        messagebox.showwarning("Name","Name Cannot Have Numbers or Special characters or Numbers")

    #     #PHONE NUMBER

    b=txt2.get()
    b1=list(txt2.get())
    testlistb=[]
    testlistb[0:10]=[''.join(b1[0:10])]

    b2=re.findall('[6-9][0-9]{9}',b)


    if testlistb ==b2:
        
        print(b)
        
    else:
        txt2.delete(0,END)
        messagebox.showwarning("Phone Number","Phone number should Contain 10 digits and cannot starts with zero")

    #         #EMAIL

    c=txt3.get()
    c1=list(c)
    testlistc=[]
    testlistc[0:100]=[''.join(c1[0:100])]

    c2=re.findall(r'\b\w+@\w+\.\w+\b',c)

    

    if testlistc==c2:
        
        print(c)
        
    else:
        txt3.delete(0,END)
        messagebox.showwarning("Email","Enter a Valid email")

            #OR

    # c3=re.findall("@gmail.com\Z",c)
    # c4=re.findall("[A-Z]",c)
    # c5=re.findall("\s",c)

    # if c3 and len(c)>10 and c4==[] and c5==[]:
    #     print(c)
    
    # else:
    #     txt3.delete(0,END)
    #     messagebox.showwarning("email","Enter a valid email")

            #PASSWORD

    d=txt4.get()
    d1=list(d)
    testlistd=[]
    testlistd[0:9]=[''.join(d1[0:9])]

    d2=re.findall('\w{8}',d)


    if testlistd ==d2:
        
        print(d)
        
    else:
        txt4.delete(0,END)
        messagebox.showwarning("Password","Enter a password ")

    #         #CONFIRM PASSWORD


    e=txt5.get()

    if e==d:
        
        print(e)
        
    else:
        txt5.delete(0,END)
        messagebox.showwarning("Confirm Password","Passwords Do not Match ")

    # if submit==1:
    #     messagebox.showinfo("Succsess","Thank you")


bt1=Button(form,text="Submit",command=submit)
bt1.place(x=610,y=180)

form.mainloop()