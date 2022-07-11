from django.shortcuts import render
from apps.paciente.models import Paciente
from django.views.generic import ListView, CreateView, UpdateView,DeleteView

class EstatisticaGeralListView(ListView):
    model = Paciente
    template_name = 'inde.html'