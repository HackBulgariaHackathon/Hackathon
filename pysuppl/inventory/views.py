from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Computer, Vendor
from datetime import datetime

def add_employee(request):
    html = "<html><body>Add employee's name:</body></html>"


def get_computers(request):

    computers = Computer.objects.all()
    return render(request, "index.html", locals())


def get_computer_info(request):
    computer_id = request.GET.get("computer_id")

    if computer_id is None:
        computer = Computer.objects.first()

    else:
        computer = get_object_or_404(Computer, pk=computer_id)

    return render(request, "computer.html", locals())
def new_computer(request):
    vendors = Vendor.objects.all()
    return render(request, "add_computer.html", locals())

def add_computer(request):
    computer_name = request.POST.get("computer_name")
    vendor_id = Vendor.objects.get(pk=request.POST.get("vendor_id"))
    serial = request.POST.get("computer_serial")
    date_bought = datetime.strptime(request.POST.get("date_bought"), '%d.%m.%Y')
    computer = Computer(name=computer_name, serial=serial, date_bought=date_bought, vendor_id=vendor_id)
    computer.save()
    return render(request, "computer.html", locals())

