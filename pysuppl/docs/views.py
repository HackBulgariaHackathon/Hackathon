from django.shortcuts import render, redirect
from .forms import DocumentForm

# Create your views here.

def upload_doc(request):
    """ DOCSTRING """
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/upload_success/')

    else:
        form = DocumentForm()

    return render(request, 'upload_doc.html', {'form':form})
