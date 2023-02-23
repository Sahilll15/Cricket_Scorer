from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def login(request):
    return render(request,'login.html')

def score(request):
    return render(request,'score.html')

def home(request):
    return HttpResponse("You are at the home page")




    