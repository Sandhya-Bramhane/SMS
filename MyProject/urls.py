"""
URL configuration for MyProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from MyProject import views
urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',views.MyHomePage),
    path('mylogin',views.MyLoginPage),
    path('mysignup',views.MySignUpPage),
    path('myadmin',views.MyAdminHome),
    path('myuser',views.MyUserHome),
    path('mystudent',views.MyStudent),
    path('mynotice',views.MyNotice),
    path('adminuser',views.AdminUser),
    path('adminuserremove',views.AdminUserRemover),
    path('adminuserupdate',views.AdminUserUpdate),
    path('studupdate',views.StudentUpdate),
    path('adminnotice',views.AdminNotice),
    path('noticedelete',views.MYNoticedelete),
    path('noteupdate',views.NoteUpdate),
    path('noticeupdate',views.NoticeUpdate),
    path('usernotice',views.MyUserNotice),
    path('hostadd',views.HostelAdd),
    path('hosteldata',views.HostelAdddata),
    path('hostelupdate',views.HostelUpdate),
    path('hostelchange',views.HostelChange),
    path('userhosteldata',views.UserHostelData),
    
   
]
