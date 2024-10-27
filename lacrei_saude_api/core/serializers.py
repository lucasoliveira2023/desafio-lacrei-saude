from rest_framework import serializers
from core.models import Profissional, Consulta, CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()

class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = '__all__'

class ConsultaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'

# Serializer para retornar detalhes do usuário
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

# Serializer para login do usuário
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()  # Corrigido de 'usename' para 'username'
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])
        if not user:
            raise serializers.ValidationError('Invalid username or password.')
        attrs['user'] = user
        return attrs

# Serializer para registro do usuário
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'first_name', 'last_name']  # Adicione outros campos conforme necessário
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
