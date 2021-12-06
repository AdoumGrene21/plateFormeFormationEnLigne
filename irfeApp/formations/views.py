from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, request

from .models import Forma

from .forms import FormationForm



def formation_view(request):
    lists_formations = Forma.objects.all()
    return render(request, 'formations/list.html', {'lists_formations': lists_formations})

def load_form(request):
    form = FormationForm
    return render(request, 'formations/form.html', {'form': form})

def add_formation(request):
    form = FormationForm(request.POST)
    form.save()
    return redirect('/formations')


def detail_formation(request, id):
    formation = Forma.objects.get(id=id)
    return render(request, 'formations/detail_formation.html', {'formation': formation})