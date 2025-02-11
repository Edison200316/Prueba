from django.shortcuts import render
from rest_framework import viewsets
from .models import Empleados, Salarios, Registros
from .serializers import EmpleadosSerializer, SalariosSerializer, RegistrosSerializer
from rest_framework.permissions import AllowAny

class EmpleadosViewSet(viewsets.ModelViewSet):
    queryset = Empleados.objects.all()
    serializer_class = EmpleadosSerializer
    permission_classes = [AllowAny]

class SalariosViewSet(viewsets.ModelViewSet):
    queryset = Salarios.objects.all()
    serializer_class = SalariosSerializer
    permission_classes = [AllowAny]

class RegistrosViewSet(viewsets.ModelViewSet):
    queryset = Registros.objects.all()
    serializer_class = RegistrosSerializer
    permission_classes = [AllowAny]

