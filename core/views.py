from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'landing.html')

def render_login(request):
    return render(request,'login.html')

def render_get_started(request):
    return render(request,'get_started.html')

def render_register(request):
    return render(request,'register.html')

def render_forgot_password(request):
    return render(request,'forgot_password.html')

def render_privacy_policy(request):
    return render(request, 'privacy_policy.html')

def render_terms_of_service(request):
    return render(request,'terms_of_service.html')