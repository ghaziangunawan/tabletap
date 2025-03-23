from django.shortcuts import render, redirect
from .forms import sign_up_form, login_form
from django.contrib.auth import login

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect("dashboard:dashboard")
    return render(request, 'landing.html')

def render_login(request):
    if request.user.is_authenticated:
        return redirect("dashboard:dashboard")
    if request.method == "POST":
        form = login_form(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard:dashboard")
        else:
            error = "email/password is not found"
        return render(request, 'login.html', {"form": login_form(), "error": error})
    return render(request,'login.html',{"form":login_form()})

def render_get_started(request):
    return render(request,'get_started.html')

def render_register(request):
    if request.user.is_authenticated:
        return redirect("dashboard:dashboard")
    if request.method == "POST":
        form = sign_up_form(request.POST)
        if form.is_valid():
            try: 
                form.save()
                return redirect("core:login")
            except:
                error = "User already created"
        else:
            error = "There is something wrong"
        return render(request, 'register.html', {"form": form, "error": error})
    else:
        return render(request,'register.html',{"form":sign_up_form()})

def render_forgot_password(request):
    return render(request,'forgot_password.html')

def render_privacy_policy(request):
    return render(request, 'privacy_policy.html')

def render_terms_of_service(request):
    return render(request,'terms_of_service.html')