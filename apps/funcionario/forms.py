from django import forms
from .models import Funcionario


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ('nome','funcao','contacto')

        widgets = {
            'nome': forms.TextInput( attrs={
                "placeholder" : "Nome Funcionario",
                "class": "form-control"
            }),
            'funcao': forms.TextInput(attrs={
                "placeholder": "Função",
                "class": "form-control"
            }),
            'contacto': forms.TextInput(attrs={
                "placeholder": "Contacto",
                "class": "form-control"
            })
        }