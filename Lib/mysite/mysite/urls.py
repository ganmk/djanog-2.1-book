"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
import main.views

urlpatterns = [
    path('admin/', admin.site.urls),
     path(r'^loginView/',main.views.loginView),
    path(r'^registView/',main.views.registView),
    path(r'^logoutView/',main.views.logoutView),
    path(r'^userBorrowedBook/',main.views.userBorrowedBook),
    path(r'^staffAddBookNum/',main.views.staffAddBookNum),
    path(r'^staffCreateBook/',main.views.staffCreateBook),
    path(r'^viewBook/',main.views.viewBook),
    path(r'^main/',main.views.main),
    path(r'^regist/',main.views.regist),
    path(r'^login/',main.views.login),
    path(r'^staffBorrowUserBook/',main.views.staffBorrowUserBook),
    path(r'^staffReturnUserBook/',main.views.staffReturnUserBook),
    path(r'^staffChangeBookInfo/',main.views.staffChangeBookInfo),
    path(r'^getTypeOptions/',main.views.getTypeOptions),
    path(r'^staffViewUser/',main.views.staffViewUser),
    path(r'^staffViewUserDetail/',main.views.staffViewUserDetail)
]
