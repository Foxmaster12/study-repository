from django.shortcuts import render
from .forms import *
# Create your views here.


def start(request):
    methods = {'actions': ['show_toys', ]}
    return render(request, 'main/base.html')


def forming(request):
    form = FirstForm()
    return render(request, 'main/form.html', {'form': form})
