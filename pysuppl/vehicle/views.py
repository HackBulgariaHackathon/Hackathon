from django.shortcuts import render
from .models import Paten_list, Vehicle
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/login')
def show_all(request):
    vehicles = Vehicle.objects.all()
    return render(request, "index.html", locals())


@login_required(login_url='/login')
def show_paten_list(request):
    paten_list = Paten_list.objects.all()
    return render(request, "paten_list.html", locals())
