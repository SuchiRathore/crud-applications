

from django.shortcuts import render
from app.models import *
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse


def index(request):
    return render(request,'index.html')

def registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = make_password(request.POST['password'])
        if User.objects.filter(email=email).exists():
            return HttpResponse("Email already exists")
        elif User.objects.filter(phone=phone).exists():
            return HttpResponse("phone already exists")
        else:
            User.objects.create(name = name, email=email, phone=phone, password=password)
            return HttpResponse("User Create")
        
        def table(request):
            data = User.objects.all()
            return render(request,"table.html",{"data":data})


# Create your views here.
