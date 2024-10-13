from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Category

def login(request: HttpRequest) -> HttpResponse:
    return render(request,"Quiz/login.html")

def signup(request: HttpRequest) -> HttpResponse:
    return render(request,"Quiz/signup.html")

def home(request: HttpRequest) -> HttpResponse:
    # collecting all the categories from db
    category_objs = Category.objects.all()

    #creating context
    context = {
        "category_objs":category_objs
    }

    return render(request,"Quiz/index.html", context=context)

def redeem(request: HttpRequest) -> HttpResponse:
    return render(request,"Quiz/redeem.html")

def quiz(request: HttpRequest) -> HttpResponse:
    return render(request,"Quiz/quiz.html")

