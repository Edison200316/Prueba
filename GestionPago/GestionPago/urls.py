"""
URL configuration for GestionPago project.

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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from EmpresaPago.views import EmpleadosViewSet, SalariosViewSet, RegistrosViewSet

# Creamos un router para manejar las rutas de la API
router = DefaultRouter()
router.register(r'empleados', EmpleadosViewSet)
router.register(r'salarios', SalariosViewSet)
router.register(r'registros', RegistrosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el panel de administración
    path('api/', include(router.urls)),  # Rutas de la API con DRF
]

