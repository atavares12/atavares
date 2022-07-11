from django.db import models
from django.contrib.auth.models import User
from apps.empresa.models import Empresa
from django.urls import reverse


class Funcionario(models.Model):
    nome = models.CharField(max_length=40)
    contacto = models.CharField(max_length=18, null=True,blank=True)
    funcao = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=True,blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


    def get_absolute_url(self):
        return reverse('list_funcionario')
