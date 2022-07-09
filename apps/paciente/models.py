from django.db import models
from django.contrib.auth.models import User
from apps.empresa.models import Empresa
from django.urls import reverse


class Paciente(models.Model):
    nome = models.CharField(max_length=40)
    nif = models.IntegerField(blank=True)
    numero_doc = models.IntegerField(blank=True)
    sexo = models.CharField(max_length=10)
    naturalidade = models.CharField(max_length=10, blank=True)
    data_nascimento = models.DateField(max_length=10, blank=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('list_paciente')
