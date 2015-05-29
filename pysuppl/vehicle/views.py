from django.shortcuts import render
from .models import Vehicle

# Create your views here.


def show_all(request):
    vehicles = Vehicle.objects.all()
    return render(request, "index.html", locals())
