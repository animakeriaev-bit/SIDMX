"""
URL configuration for sidapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app.views import principal, servicios, portafolio, nosotros, contacto, construccion, remodelacion, mantenimiento,gestion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',principal, name ="home"),
    path('servicios/',servicios, name="servicios"),
    path('portafolio/', portafolio, name="portafolio"),
    path('nosotros/', nosotros , name="nosotros"),
    path('contacto/', contacto, name="contacto"),
    path('construccion/', construccion, name="construccion"),
    path('remodelacion/', remodelacion, name="remodelacion"),
    path('mantenimiento/', mantenimiento, name='mantenimiento'),
    path('gestion/', gestion, name="gestion")
] 
