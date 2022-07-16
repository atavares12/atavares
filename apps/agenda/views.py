from django.shortcuts import render

# Create your views here.


def agenda(request):
    context = {

    }
    return render(request, 'agenda/agenda.html', context=context)
