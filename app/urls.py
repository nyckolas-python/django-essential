"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# disable user_proxy.views to use user_profile.views
# from user_proxy.views import Index, CreateUser, AllUsers
from user_profile.views import Index, CreateUser, AllUsers, UpdateProfile

from app.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name="index"),
    path('signup/', CreateUser.as_view(), name="signup"),
    path('all_users/', AllUsers.as_view(), name="all_users"),
    path('profile/<pk>', UpdateProfile.as_view(), name='profile'),
    path('front/', include('nyckolas_frontend.urls')),
    path('', include('jinja_app.urls')),
    path('', include('email_app.urls')),
    # path('', include('reset_password_app.urls'))
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
