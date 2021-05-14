from typing import AsyncIterable
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/reset_password.html'), name='rest_password'),

    path('rest_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_sent.html'), name='password_reset_done'),

    path('rest/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_form.html'), name='password_reset_confirm'),

    path('rest_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_complete'),



    # passworld changes
    path('change-password/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    #path('change-password-done/', auth_views.)


    # sign-up and sign-in
    path('sign-up/', views.sign_up, name='sign-up'),
    
    path('sign-in/', auth_views.LoginView.as_view(template_name='sign_in.html'), name='sign-in'),

    path('sign-out/', auth_views.LogoutView.as_view(template_name='sign-out.html'), name='sign-out')

]