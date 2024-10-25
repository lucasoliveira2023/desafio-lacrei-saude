from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from core.models import Profissional

class ProfissionalTests(APITestCase):
    
    def setUp(self):
        # Configurações iniciais para os testes (executado antes de cada teste)
        self.profissional_data = {
            "nome_completo": "Maria Silva",
            "profissao": "Médico",
            "endereco": "Rua A, 123",
            "contato": "123456789",
            "nome_social": "Dra. Maria"
        }
        self.profissional = Profissional.objects.create(**self.profissional_data)

    def test_get_profissionais(self):
        # Testa o endpoint de listar profissionais
        url = reverse('profissional-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Verifica se há um profissional listado

    def test_create_profissional(self):
        # Testa o endpoint de criar um novo profissional
        url = reverse('profissional-list')
        new_profissional = {
            "nome_completo": "João Pereira",
            "profissao": "Fisioterapeuta",
            "endereco": "Rua B, 456",
            "contato": "987654321",
            "nome_social": "Dr. João"
        }
        response = self.client.post(url, new_profissional, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profissional.objects.count(), 2)  # Verifica se foi criado um novo profissional

    def test_get_single_profissional(self):
        # Testa o endpoint de obter um profissional específico
        url = reverse('profissional-detail', args=[self.profissional.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome_completo'], self.profissional.nome_completo)

    def test_update_profissional(self):
        # Testa o endpoint de atualizar um profissional existente
        url = reverse('profissional-detail', args=[self.profissional.id])
        updated_data = {
            "nome_completo": "Maria Silva Atualizado",
            "profissao": "Médico",
            "endereco": "Rua A, 123",
            "contato": "123456789",
            "nome_social": "Dra. Maria Atualizado"
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.profissional.refresh_from_db()
        self.assertEqual(self.profissional.nome_completo, "Maria Silva Atualizado")

    def test_delete_profissional(self):
        # Testa o endpoint de deletar um profissional
        url = reverse('profissional-detail', args=[self.profissional.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Profissional.objects.count(), 0)  # Verifica se o profissional foi deletado
