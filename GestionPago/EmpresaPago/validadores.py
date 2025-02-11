from django.core.exceptions import ValidationError
import re

def validacion_numeros(value):
    """
    Validador para asegurarse de que el campo contenga solo números.
    """
    if not re.fullmatch(r'^\d+$', value):
        raise ValidationError("Este campo solo puede contener números.")

def validar_telefono(value):
    """
    Validador para asegurarse de que el número de teléfono tenga entre 7 y 15 dígitos.
    """
    if not re.fullmatch(r'^\d{7,15}$', value):
        raise ValidationError("El número de teléfono debe contener entre 7 y 15 dígitos.")

def validar_cedula(value):
    """
    Validador para asegurarse de que la cédula tenga exactamente 10 dígitos.
    """
    if not re.fullmatch(r'^\d{10}$', value):
        raise ValidationError("La cédula debe contener exactamente 10 dígitos.")
