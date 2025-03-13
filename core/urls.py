from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('', views.index, name='index'),
    path('get_started/', views.render_get_started, name='get_started'),
    path('login/', views.render_login, name='login'),
    path('register/',views.render_register,name='register'),
    path('forgot-password/',views.render_forgot_password,name='forgot_password'),
    path('privacy-policy/',views.render_privacy_policy,name='privacy_policy'),
    path('terms-of-service/',views.render_terms_of_service,name='terms_of_service'),
]