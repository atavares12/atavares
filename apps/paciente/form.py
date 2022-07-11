from django import forms
from .models import Paciente


SEXO_CHOICES = (
    ('M','Masculino'),
    ('F','Feminio')
)


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ('nome','nif','numero_doc','sexo','naturalidade','data_nascimento')

        widgets = {
            'nome': forms.TextInput( attrs={
                "placeholder" : "Nome Paciente",
                "class": "form-control"
            }),
            'data_nascimento': forms.TextInput(attrs={
                "placeholder": "Data Nascimento",
                "class": "form-control"
            }),
            'sexo': forms.TextInput(attrs={
                "placeholder": "Sexo",
                "class": "form-control"
            }),
            'naturalidade': forms.TextInput(attrs={
                "placeholder": "Naturalidade",
                "class": "form-control"
            }),
            'nif': forms.TextInput(attrs={
                "placeholder": "NIF",
                "class": "form-control"
            }),
            'numero_doc': forms.TextInput(attrs={
                "placeholder": "Numero Documento",
                "class": "form-control"
            })
        }