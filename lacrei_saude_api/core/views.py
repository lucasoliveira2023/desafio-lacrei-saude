from django.shortcuts import render
from rest_framework import viewsets
from core.models import Profissional, Consulta
from core.serializers import ProfissionalSerializer, ConsultaSerializers
# Create your views here.

class ProfissionalViewSet(viewsets.ModelViewSet):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer
    
class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializers
