from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
# Create your views here.

def index(request):
    return render(request,'homepage.html')

def All_Carlist(request):
    cars=Car.objects.all()
    return render(request,'All_Carlist.html',{'cars':cars})
