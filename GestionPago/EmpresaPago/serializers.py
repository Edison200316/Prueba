from rest_framework import serializers
from .models import Empleados, Salarios, Registros

class EmpleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = '__all__'  
        
class SalariosSerializer(serializers.ModelSerializer):
    empleado = EmpleadosSerializer(read_only=True) 
    empleado_id = serializers.PrimaryKeyRelatedField(queryset=Empleados.objects.all(), source='empleado', write_only=True)

    class Meta:
        model = Salarios
        fields = ['id', 'empleado', 'empleado_id', 'salario_base', 'bono', 'fecha_actualizacion']

class RegistrosSerializer(serializers.ModelSerializer):
    empleado = EmpleadosSerializer(read_only=True)  
    empleado_id = serializers.PrimaryKeyRelatedField(queryset=Empleados.objects.all(), source='empleado', write_only=True)

    class Meta:
        model = Registros
        fields = ['id', 'empleado', 'empleado_id', 'fecha_registro', 'tipo_registro']
