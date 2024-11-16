from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def login(request: HttpRequest) -> HttpResponse:
    return render(request,"Quiz/login.html")

def signup(request: HttpRequest) -> HttpResponse:
    return render(request,"Quiz/signup.html")

def home(request: HttpRequest) -> HttpResponse:
    context = {
        "admin":request.user.is_superuser
    }
    return render(request,"Quiz/index.html", context)

def redeem(request: HttpRequest) -> HttpResponse:
    return render(request,"Quiz/redeem.html")

def quiz(request: HttpRequest) -> HttpResponse:
    return render(request,"Quiz/quiz.html")

