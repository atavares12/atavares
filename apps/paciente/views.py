from django.views.generic import ListView, CreateView, UpdateView
from .models import Paciente
from .form import PacienteForm


class PacienteList(ListView):
    model = Paciente

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Paciente.objects.filter(empresa=empresa_logada)


class PacienteCreate(CreateView):
    model = Paciente
    form_class = PacienteForm

    def form_valid(self, form):
        paciente = form.save(commit=False)
        paciente.empresa = self.request.user.funcionario.empresa
        paciente.criador_por = self.request.user.funcionario.user
        paciente.save()
        return super(PacienteCreate, self).form_valid(form)

class PacienteUpdate(UpdateView):
    model = Paciente
    template_name = 'paciente/paciente_update.html'
    fields = ('nome','data_nascimento','naturalidade','sexo','numero_doc','nif')