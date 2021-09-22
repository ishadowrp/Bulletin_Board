"""BulletinBoard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic.base import TemplateView
from BB.views import PostList, HomePageView, AboutPageView, ContactsPageView
from accounts.views import SignupPageView, LoginPageView, LogoutPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('posts/', include('BB.urls')),  # делаем так, чтобы все адреса из нашего приложения (news/urls.py) сами автоматически подключались когда мы их добавим.
    path('accounts/signup/', SignupPageView.as_view(), name='account_signup'),
    path('accounts/login/', LoginPageView.as_view(), name='account_login'),
    path('accounts/logout/', LogoutPageView.as_view(), name='account_logout'),
    path('accounts/', include('allauth.urls')),
    path('', PostList.as_view()),
]
