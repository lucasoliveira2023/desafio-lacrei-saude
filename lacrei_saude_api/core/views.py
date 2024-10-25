from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from core.models import Profissional, Consulta
from core.serializers import ProfissionalSerializer, ConsultaSerializers, UserSerializer, UserRegisterSerializer, UserLoginSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from django.contrib.auth import get_user_model
# Create your views here.

#class ProfissionalViewSet(viewsets.ModelViewSet):
#    queryset = Profissional.objects.all()
#    serializer_class = ProfissionalSerializer
    

#class ConsultaViewSet(viewsets.ModelViewSet):
#   queryset = Consulta.objects.all()
#   serializer_class = ConsultaSerializers

class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    
class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer
    
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        if user:
            return Response({'message':'Login successful!'}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status= status.HTTP_400_BAD_REQUEST)
    
class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    
def get_object(self):
    return self.request.user #retorna usuario autenticado

def get(self, request):
    user = self.get_object()
    serializer = UserSerializer(user)
    return Response(serializer.data)

def put(self, request):
    user = self.get_object()
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(self, request):
    user = self.get_object()
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class ProfissionalList(APIView):
    ##lista todos os profissiopnais e cria novos profissioais
    
    def get(self, request):
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