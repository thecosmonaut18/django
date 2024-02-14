from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from myapp.form import EmpForm,studform
from myproject import settings
from django.core.mail import send_mail

# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello Guys</h1>")

def fun(request):
    return HttpResponse("<h1>Hellohello</h1>")
def run(request):
    return HttpResponse("hello world")
def myHTML(request):
    temp=loader.get_template("day1.html")
    name=input('Enter Your Name : ')
    details={'fname':name}
    return HttpResponse(temp.render(details))

def reg_emp(request):
    if request.method=="POST":
        frm=EmpForm(request.POST)
        # print("__________________________________________")
        # print(frm)
        # return HttpResponse("Sett ahn machane")
        if frm.is_valid():
            try:
                return redirect("/")
            except:
                return HttpResponse("error")
            # print("==")
    else:
        # print("///////////////////////////////////////////")
        emp=EmpForm()
        return render(request,'emp_reg.html',{'form':emp})
    
def stud_reg(request):
    s=studform()
    return render(request,'stud_reg.html',{'stud':s})

def about(request):
    return render(request,'about.html')

def set_c(request):
    res=HttpResponse('cookies set')
    res.set_cookie('name','anu')
    return res

def get_c(request):
    ename=request.COOKIES['name']
    return HttpResponse('my name is '+ename)

def mail(request):
    subject="welcome"
    msg="hai django"
    to="jilsonantony2@gmail.com"
    res=send_mail(subject,msg,settings.EMAIL_HOST_USER,[to])
    if res==1:
        m="Success"
    else:
        m="Failed"
    return HttpResponse(m)