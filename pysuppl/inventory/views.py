from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Computer, Vendor, Software, License
from .forms import ComputerForm
from .forms import SoftwareForm
from datetime import datetime
from django.contrib.auth.models import Group, User


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
    owners = User.objects.all()
    return render(request, "add_computer.html", locals())


def add_computer(request):
    computer_name = request.POST.get("computer_name")
    vendor_id = Vendor.objects.get(pk=request.POST.get("vendor_id"))
    serial = request.POST.get("computer_serial")
    date_bought = datetime.strptime(request.POST.get("date_bought"), '%d.%m.%Y')
    owner = User(request.POST.get("owner_email"))
    computer = Computer(name=computer_name, serial=serial, date_bought=date_bought, owner=owner, vendor_id=vendor_id)
    computer.save()
    return redirect('/inventory/computers')


def delete_computer(request, computer_id):
    computer = get_object_or_404(Computer, pk=computer_id)
    computer.delete()
    return redirect('/inventory/computers')


def edit_computer(request, computer_id):
    computer = get_object_or_404(Computer, pk=computer_id)
    form = ComputerForm(instance=computer)
    if request.POST:
        form = ComputerForm(request.POST, instance=computer)
        if form.is_valid():
            form.save()

            return redirect('/inventory/computers')

    return render(request, 'edit_computer.html', locals())


def get_software(request):
    all_software = Software.objects.all()
    return render(request, 'show_software.html', locals())


def get_software_info(request):
    software_id = request.GET.get("software_id")
    if software_id is None:
        software = Software.objects.first()
    else:
        software = get_object_or_404(Software, pk=software_id)
    return render(request, "software.html", locals())


def add_software(request):
    software_name = request.POST.get("software_name")
    description = request.POST.get("description")
    vendor = request.POST.get("vendor")
    license = request.POST.get("license")
    # installed = Software.objects.get.
    computer_id = Software.objects.get(name=software_name)
    all_computers = Software.objects.all()
    installed = Computer.objects.get(pk=request.POST.get("computer_id"))

    installed.software_set.all()


    software = Software(name=software_name, description=description,
        vendor_id=vendor, license_id=license, installed=installed)
    software.save()
    return redirect('/inventory/all_software')

