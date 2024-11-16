from django.urls import path, include
from . import views

urlpatterns = [
    path("signup/",views.signup, name="signup"),
    path("login/",views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    
    path("",views.home, name="home"),
    path("redeem/",views.redeem, name="redeem"),
    path("quiz/",views.quiz, name="quiz"),
]