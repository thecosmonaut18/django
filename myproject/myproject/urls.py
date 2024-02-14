"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myapp import views
from stud import views as st

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", include("myapp.urls")),
    path("h/",st.hi),
    path("reg/",st.stud_add),
    path("view/",st.view_stud),
    path("de/<int:sid>/",st.det_stud),
    path("edit/<int:sid>/",st.edit_stud),
    path("update/<int:sid>/",st.update_stud),
    path("ssu/",st.stud_SignUp),
    path("tsu/",st.teach_signup),
    path("emp/",st.employee),
    path("ve/",st.view_employee),
    path("sm/",st.sign_in),
    path("ah/",st.admin_home),
    path("sh/",st.stud_home),

]
