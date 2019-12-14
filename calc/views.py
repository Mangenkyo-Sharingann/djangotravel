from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    #n1 = request.POST['loop']
    return render(request,'home.html',{'name':'Iyer'})#for joining the template render is used


def add(request):
    val1 = int(request.POST['num1']) #values taken are by default is string 
    val2 = int(request.POST['num2']) # so you hav to type convert and use single quotes only
    res = val1 + val2
    return render(request, "result.html",{'result':res})#from here the values goes to the result.html where it is displayed 