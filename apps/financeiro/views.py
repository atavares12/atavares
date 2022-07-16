from django.shortcuts import render

# Create your views here.


def visaoGeral(request):
    context = {

    }
    return render(request, 'financeiro/visao_geral.html', context=context)
