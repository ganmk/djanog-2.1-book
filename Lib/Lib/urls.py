
from django.contrib import admin
from django.urls import path
import main.views

urlpatterns = [
     path('admin/', admin.site.urls),
     path('loginView/',main.views.loginView),
    path('registView/',main.views.registView),
    path('logoutView/',main.views.logoutView),
    path('userBorrowedBook/',main.views.userBorrowedBook),
    path('staffAddBookNum/',main.views.staffAddBookNum),
    path('staffCreateBook/',main.views.staffCreateBook),
    path('viewBook/',main.views.viewBook),
    path('main/',main.views.main),
    path('regist/',main.views.regist),
    path('login/',main.views.login),
    path('staffBorrowUserBook/',main.views.staffBorrowUserBook),
    path('staffReturnUserBook/',main.views.staffReturnUserBook),
    path('staffChangeBookInfo/',main.views.staffChangeBookInfo),
    path('getTypeOptions/',main.views.getTypeOptions),
    path('staffViewUser/',main.views.staffViewUser),
    path('staffViewUserDetail/',main.views.staffViewUserDetail)
]