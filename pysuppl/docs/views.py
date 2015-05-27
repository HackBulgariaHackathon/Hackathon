#! -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .forms import DocumentForm

# Create your views here.



def upload(request):

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            print("###############")
            print(request.user)
            print(request.POST)
            print("-------------")
            print(request.FILES)
            print("***************************")
            print(request.FILES['file'])
            print("###############")
            form.save()
            return redirect('/admin')

    else:
        form = DocumentForm()

    return render(request, 'upload_doc.html', {'form': form})
