from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import Profissional, Consulta
from core.serializers import ProfissionalSerializer, ConsultaSerializers
from django.http import Http404
# Create your views here.

#class ProfissionalViewSet(viewsets.ModelViewSet):
#    queryset = Profissional.objects.all()
#    serializer_class = ProfissionalSerializer
    

#class ConsultaViewSet(viewsets.ModelViewSet):
#   queryset = Consulta.objects.all()
#   serializer_class = ConsultaSerializers

class ProfissionalList(APIView):
    ##lista todos os profissiopnais e cria novos profissioais
    
    def get_pro(self, request):
        profissionais = Profissional.objects.all()
        serializer = ProfissionalSerializer(profissionais, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProfissionalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ProfissionalDetail(APIView):
    ## Recuperar, atualiza ou deleta um profissional especifico.
    
    def get_object(self, id):
        try:
            return Profissional.objects.get(pk=id)
        except Profissional.DoesNotExist:
            raise Http404
        
    def get(self, request, id):
        profissional = self.get_object(id)
        serializer = ProfissionalSerializer(profissional)
        return Response(serializer.data)
    
    def put(self, request, id):
        profissional = self.get_object(id)
        serializer = ProfissionalSerializer(profissional, data=request.data)
        if serializer .is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        profissional = self.get_object(id)
        profissional.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)