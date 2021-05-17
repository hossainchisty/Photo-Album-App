from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('sign-up/', views.register,name="register"),
    path('sign-in/', auth_views.LoginView.as_view(template_name='login.html'),name="login"),
    path('sign-out/', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout")

]
# ratul
# /A=wz2pZp#e!"x5m