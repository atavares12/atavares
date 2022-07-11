from django.db import models
from django.contrib.auth.models import User
from apps.funcionario.models import Funcionario
from apps.empresa.models import Empresa
from django.urls import reverse


SEXO_CHOICES = (
    ('M','Masculino'),
    ('F','Feminio')
)

class Paciente(models.Model):
    nome = models.CharField(max_length=40)
    nif = models.IntegerField(blank=True)
    numero_doc = models.IntegerField(blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    naturalidade = models.CharField(max_length=10, blank=True)
    data_nascimento = models.DateField(max_length=10, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    criador_por = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


    def get_absolute_url(self):
        return reverse('list_paciente')
