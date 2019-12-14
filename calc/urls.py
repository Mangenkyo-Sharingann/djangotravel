#pat('lokupfunction_name',views.func_nme,name="userwish_name")

from django.urls import path

from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path("add",views.add,name="add")
    
]
