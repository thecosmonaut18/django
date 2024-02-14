from django.urls import path
from myapp import views

urlpatterns = [
    path("i/",views.index),
    path("f/",views.fun),
    path("r/",views.run),
    path("my/",views.myHTML),
    path("em/",views.reg_emp),
    path("a/",views.about),
    path("sc/",views.set_c),
    path("gc/",views.get_c),
    path("m/",views.mail),
]