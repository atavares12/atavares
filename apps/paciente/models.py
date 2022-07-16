from django.db import models
from django.contrib.auth.models import User
from apps.funcionario.models import Funcionario
from apps.empresa.models import Empresa
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


SEXO_CHOICES = (
    ('M','Masculino'),
    ('F','Feminio')
)

def validate_even(value):
    if value == 0:
        raise ValidationError(
            _('Nao pode ser zero'),
            params={'value': value},
        )

class Paciente(models.Model):
    nome = models.CharField(max_length=40)
    nif = models.IntegerField(null=True,blank=True,validators=[validate_even])
    numero_doc = models.IntegerField(blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    naturalidade = models.CharField(max_length=10, blank=True)
    data_nascimento = models.DateField(max_length=10, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    criador_por = models.ForeignKey(User, on_delete=models.CASCADE)
    fator_sanguino = models.CharField(max_length=5, blank=True)
    criado_em = models.CharField(max_length=8, blank=True)
    etnia = models.CharField(max_length=10, blank=True)
    mae = models.CharField(max_length=40, blank=True)
    pai = models.CharField(max_length=40, blank=True)
    escolaridade = models.CharField(max_length=25, blank=True)
    profissao = models.CharField(max_length=25, blank=True)
    entidade_patronal = models.CharField(max_length=25, blank=True)
    obs =models.TextField(blank=True)

    def __str__(self):
        return self.nome


    def get_absolute_url(self):
        return reverse('list_paciente')

