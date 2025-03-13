from django.shortcuts import render

# Create your views here.
def render_menu(request):
    return render(request,"menu.html")