from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Vehicle

# Create your views here.


@login_required(login_url='/login')
def show_all(request):
    vehicles = Vehicle.objects.all()
    return render(request, "index.html", locals())
