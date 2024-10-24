from django.db import models

# Create your models here.
class Profissional(models.Model):
    nome_completo = models.CharField(max_length=255)
    nome_social = models.CharField(max_length=255, blank=True, null= True)
    profissao = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    contato = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.nome_completo
    
    
class Consulta(models.Model):
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    data = models.DateField()
    
    
    def __str__(self):
        return f"{self.profissional.nome_completo} - {self.data}"