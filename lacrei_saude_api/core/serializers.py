from rest_framework import serializers
from core.models import Profissional, Consulta

class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = '__all__'
        
class ConsultaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'