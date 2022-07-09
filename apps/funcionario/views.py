from django.views.generic import ListView, CreateView, UpdateView
from .models import Funcionario
from .forms import FuncionarioForm


class FuncionarioList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)

class FuncionarioCreate(CreateView):
    model = Funcionario
    form_class = FuncionarioForm

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.save()
        return super(FuncionarioCreate, self).form_valid(form)

class FuncionarioUpdate(UpdateView):
    model = Funcionario
    template_name = 'funcionario/funcionario_update.html'
    fields = ('nome','funcao','contacto')


