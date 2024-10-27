from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from core.models import Profissional, Consulta
from core.serializers import (
    ProfissionalSerializer,
    UserSerializer,
    UserRegisterSerializer,
    UserLoginSerializer
)
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework_simplejwt.tokens import RefreshToken


# View para registro de usuários
class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer


# View para login de usuários
class UserLoginView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Autenticação do usuário
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        
        if user:
            # Geração do token de refresh e access
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'message': 'Login successful!'
            }, status=status.HTTP_200_OK)
        
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


# View para detalhes do usuário autenticado
class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user  # Retorna o usuário autenticado

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
        return Response({"message":"usuario deletado com sucesso"} ,status=status.HTTP_204_NO_CONTENT)


# View para listar e criar profissionais
class ProfissionalList(APIView):
    permission_classes = [IsAuthenticated]  # Proteger a view com autenticação

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


# View para detalhes de um profissional específico
class ProfissionalDetail(APIView):
    permission_classes = [IsAuthenticated]

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
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        profissional = self.get_object(id)
        profissional.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
