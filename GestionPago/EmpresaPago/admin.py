from django.contrib import admin
from .models import Empleados, Salarios, Registros

@admin.register(Empleados)
class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ("cedula", "nombre", "apellido", "email", "telefono", "tipo")
    search_fields = ("cedula", "nombre", "apellido", "email")
    list_filter = ("tipo",)

@admin.register(Salarios)
class SalariosAdmin(admin.ModelAdmin):
    list_display = ("empleado", "salario_base", "bono", "fecha_actualizacion")
    search_fields = ("empleado__nombre", "empleado__apellido")
    list_filter = ("fecha_actualizacion",)

@admin.register(Registros)
class RegistrosAdmin(admin.ModelAdmin):
    list_display = ("empleado", "fecha_registro", "tipo_registro")
    search_fields = ("empleado__nombre", "empleado__apellido")
    list_filter = ("tipo_registro", "fecha_registro")
