from django.db import models
from .choices import TIPO, TIPOS_REGISTRO
from django.core.validators import MinLengthValidator, EmailValidator
from .validadores import validacion_numeros, validar_telefono, validar_cedula, validar_email

class Empleados(models.Model):
    cedula = models.CharField(max_length=10, primary_key=True, validators=[validar_cedula])
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator(), validar_email],unique=True)
    telefono = models.CharField(max_length=15, validators=[validar_telefono])
    tipo = models.CharField(max_length=50, choices=TIPO)

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        db_table = "Empleados"
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Salarios(models.Model):
    empleado = models.OneToOneField(Empleados, on_delete=models.CASCADE, related_name="salario")
    salario_base = models.DecimalField(max_digits=10, decimal_places=2)
    bono = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)
    fecha_actualizacion = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Salario"
        verbose_name_plural = "Salarios"
        db_table = "Salarios"

    def __str__(self):
        return f"Salario de {self.empleado.nombre} {self.empleado.apellido}"

class Registros(models.Model):
    empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE, related_name="registros")
    fecha_registro = models.DateField(auto_now_add=True)
    tipo_registro = models.CharField(max_length=100, choices=TIPOS_REGISTRO)

    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"
        db_table = "Registros"

    def __str__(self):
        return f"Registro de {self.empleado.nombre} el {self.fecha_registro}"


