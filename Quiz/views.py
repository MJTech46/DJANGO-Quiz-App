from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def login(request: HttpRequest) -> HttpResponse:
    return render(request,"Quiz/login.html")

def home(request: HttpRequest) -> HttpResponse:
    return render(request,"Quiz/index.html")

def redeem(request: HttpRequest) -> HttpResponse:
    return render(request,"Quiz/redeem.html")

def quiz(request: HttpRequest) -> HttpResponse:
    return render(request,"Quiz/quiz.html")

