from django.shortcuts import render,redirect
from django.http import HttpResponse
from stud.form import StudentForm
from stud.models import Student,User,Employee,Stud_User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def hi(request):
    return HttpResponse('<h1>hi student</h1>')


def stud_add(request):
    if request.method=="POST":
        stufrm=StudentForm(request.POST)
        if stufrm.is_valid():
            stufrm.save()
            # return redirect('/view')
            # return HttpResponse("<h1>Success</h1>")
            return HttpResponse("<script>window.alert('Successfully added!!');window.location.href='/view'</script>")
        else:
            return HttpResponse("<h1>Failed</h1>")
    else:
        stu=StudentForm()
        return render(request,'stud1_reg.html',{'form':stu})
    

def view_stud(request):
    details=Student.objects.all()
    return render(request,'views_stud.html',{'data':details})


def det_stud(request,sid):
    print("_______________",sid)
    stu=Student.objects.get(id=sid)
    stu.delete()
    return HttpResponse("<script>window.alert('Successfully deleted!!');window.location.href='/view'</script>")

    # return HttpResponse("<h1>Deleted</h1>")


def edit_stud(request,sid):
    print("---------------",sid)
    stu=Student.objects.get(id=sid)
    return render(request,'edit_stud.html',{'data':stu})

def update_stud(request,sid):
    st=Student.objects.get(id=sid)
    form=StudentForm(request.POST,instance=st)
    if form.is_valid():
        form.save()
        return HttpResponse("<script>window.alert('succesfully updated');window.location.href='/view'</script>")
    else:
       return HttpResponse("<script>window.alert('error Occured');window.location.href='/view'</script>")

    # return HttpResponse("<scripts>Successfully Updated</script>")

def stud_SignUp(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        user=request.POST.get("uname")
        phn=request.POST['ph']
        pw=request.POST['passw']

        # print("_________________",user,email)

        user_details=User.objects.create_user(first_name=fname,
                                 last_name=lname,
                                 email=email,
                                 username=user,
                                 phone=phn,
                                 password=pw,
                                 usertype='Student'
                                 )
        user_details.save()

        dpt=request.POST['dpt']
        pm=request.POST['pm']

        details=Stud_User.objects.create(department=dpt,plus_mark=pm,user_id=user_details)
        details.save()

        return HttpResponse("<script>window.alert('succesfully Saved')</script>")
    else:
        return render(request,'SignUp.html')
    

def teach_signup(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        user=request.POST.get("uname")
        phn=request.POST['ph']
        pw=request.POST['passw']

        # print("_________________",user,email)

        User.objects.create_user(first_name=fname,
                                 last_name=lname,
                                 email=email,
                                 username=user,
                                 phone=phn,
                                 password=pw,
                                 usertype='Teacher'
                                 )
        return HttpResponse("<script>window.alert('succesfully Saved')</script>")
    else:
        return render(request,'teach_signup.html')
    
def employee(request):
        if request.method=="POST":
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            age=request.POST['age']
            email=request.POST['email']
            username=request.POST.get("username")
            phone=request.POST['phone']
            password=request.POST['password']
            x=Employee.objects.create(first_name=firstname,
                                 last_name=lastname,
                                 age=age,
                                 email=email,
                                 username=username,
                                 phone=phone,
                                 password=password)
            x.save()
            return HttpResponse("<script>window.alert('succesfully Saved')</script>")
        else:
            return render(request,'employ.html')

def view_employee(request):
    details=Employee.objects.all()
    return render(request,'view_employee.html',{"data":details})


def sign_in(request):
    if request.method=="POST":
        uname=request.POST['uname']
        passw=request.POST['passw']
        vv=authenticate(username=uname,password=passw)
        if vv is not None:
            return render("<script>window.alert('succesful LOGIN')</script>")
        else:
             return render("<script>window.alert('InCorrect Password or Username')</script>")           
    else:
        return render(request,'signin.html')

def admin_home(request):
    return render(request,'admin_home.html')

def stud_home(request):
    return render(request,'stud_home.html')
