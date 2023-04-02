from django.contrib import admin
from django.urls import path, include

from .views import MyTemplateView, usersignup, activate_account, subscription
from django.contrib.auth import views as auth

urlpatterns = [
    path('test-mail/', MyTemplateView.as_view(), name='test-mail'),
    path('logout/', auth.LogoutView.as_view(template_name='index.html'),
         name='logout'),
    path(r'sign-up/', usersignup, name='register_user'),
    path(
        r'activate/<uidb64>/<token>/',
        activate_account, name='activate'),
    path("subscription/", subscription, name="subscription"),
]
