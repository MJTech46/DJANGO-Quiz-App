from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from Account.models import CustomUser
from .models import Reward, Quiz, Option
from .utils import create_default_rewards_once
from .utils import create_default_quizzes_once

from random import choice as random_choice
from random import sample as random_sample
from json import dumps as json_dumps

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

    if request.method == "GET":
        create_default_quizzes_once()
        
        q = Quiz.objects.all()
        q = random_choice(q)

        o = list(Option.objects.filter(quiz = q.pk))
        o = random_sample(o, len(o))
        o = enumerate(o, start=1)

        context = {
            "quiz": q,
            "options": o
        }
        return render(request,"Quiz/quiz.html", context)
    
    if request.method == "POST":
        quiz_pk = request.POST.get("quizPK")
        option_pk = request.POST.get("optionPK")

        user = request.user

        # Adding points to the user account
        is_true = Option.objects.get(pk=option_pk).is_correct
        if is_true:
            user_obj = CustomUser.objects.get(pk=user.pk)
            user_obj.lifeTime_coins = user_obj.lifeTime_coins + 50
            user_obj.current_coins = user_obj.current_coins + 50
            user_obj.save()

        response = json_dumps({
            "is_true": is_true
        })

        print(f"{quiz_pk=}\n{option_pk=}\n{user=}\n{response=}")

        return JsonResponse(response)

