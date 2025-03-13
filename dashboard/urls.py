from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("",views.render_dashboard,name="dashboard")
]