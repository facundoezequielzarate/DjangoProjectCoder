"""CoderProject URL Configuration

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
from django.urls import path
from CoderProject.views import familiares
from CoderProject.views import texto
from CoderProject.views import madree
from CoderProject.views import padree
from CoderProject.views import hermanoo
from CoderProject.views import hermanaa
from CoderProject.views import saludo_con_nombre_y_fecha
from CoderProject.views import template_familiares

urlpatterns = [
    path("admin/", admin.site.urls),
    path("familiares/", familiares),
    path("texto/", texto),
    path("madre/", madree),
    path("padre/", padree),
    path("hermano/", hermanoo),
    path("hermana/", hermanaa),
    path("saludo-con-datetime/<nombre>/", saludo_con_nombre_y_fecha),
    path("familia/", template_familiares),
    ]
