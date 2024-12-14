from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from Account.models import CustomUser
from .models import Reward, Quiz, Option
from .utils import create_default_rewards_once
from .utils import create_default_quizzes_once

from random import choice


def login(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request,"Quiz/login.html")
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect("home")
        else:
            return render(request,"Quiz/login.html", {"message":"Wrong credentials. please check!"})

def signup(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request,"Quiz/signup.html")
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        re_password = request.POST.get("re-password")
        try:
            if  password == re_password:
                CustomUser.objects.create_user(username=username, password=password)
                return redirect("login")
            else:
                return render(request,"Quiz/signup.html", {"message":"Password doesn't mach. please check!"})
        except Exception as e:
                return render(request,"Quiz/signup.html", {"message":"User already exist !"})


@login_required(login_url="login")
def logout(request: HttpRequest) -> HttpResponse:
    auth_logout(request)
    return redirect("login")

@login_required(login_url="login")
def home(request: HttpRequest) -> HttpResponse:
    context = {
        "admin":request.user.is_superuser
    }
    return render(request,"Quiz/index.html", context)


@login_required(login_url="login")
def redeem(request: HttpRequest) -> HttpResponse:
    create_default_rewards_once()
    context={
        "rewards" : Reward.objects.all()
    }
    return render(request,"Quiz/redeem.html", context)


@login_required(login_url="login")
def quiz(request: HttpRequest) -> HttpResponse:
    # q = Quiz.objects.all()
    # context = {
    #     "quiz_text": choice(q)
    # }
    create_default_quizzes_once()
    return render(request,"Quiz/quiz.html")

