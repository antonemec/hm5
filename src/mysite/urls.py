"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from first_app.views import *

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('gen-student/', generate_student),
    path('students/', students),
    path('students/add/', students_add),
    path('gen-group/', generate_group),
    path('groups/', groups),
    path('groups/add/', groups_add),
    path('gen-teacher/', generate_teacher),
    path('teachers/', teachers),
    path('teachers/add/', teachers_add),
]
