from django.shortcuts import render
from .models import Paten_list, Vehicle

# Create your views here.


def show_all(request):
    vehicles = Vehicle.objects.all()
    return render(request, "index.html", locals())


def show_paten_list(request):
    paten_list = Paten_list.objects.all()
    return render(request, "paten_list.html", locals())
