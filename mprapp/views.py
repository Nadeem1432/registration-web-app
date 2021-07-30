from django.shortcuts import render, HttpResponse
from .models import Table

# Create your views here.

def home(request):
    # return  HttpResponse('home page')
    if request.method =='POST':
        name  = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date  = request.POST['date']
        t= Table(name = name , email = email ,phone = phone , date = date)

        t.save()
        var1 = True
        # return  HttpResponse('data submitted..')
        return render(request,'mprapp/home.html',{'var1':var1})


    return render(request,'mprapp/home.html')