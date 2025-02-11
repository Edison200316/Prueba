from django.core.exceptions import ValidationError
import re

def validar_email(value):
    """
    Valida que el email tenga un formato correcto y pertenezca a un dominio válido.
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    
    if not re.match(email_regex, value):
        raise ValidationError("El formato del correo electrónico no es válido.")
    
    dominios_permitidos = ["gmail.com", "outlook.com", "empresa.com"]
    dominio = value.split("@")[-1]

    if dominio not in dominios_permitidos:
        raise ValidationError(f"El dominio '{dominio}' no está permitido. Usa uno de estos: {', '.join(dominios_permitidos)}")
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
