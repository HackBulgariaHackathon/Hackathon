from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import UserGro
# Create your views here.



#def docs(request):
#    current_user = request.user
#    department_id = Group.objects.filter(jkkkkk)
#    docs = Document.objects.all
#

@login_required
def upload(request):

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            print("###############")
            print(request.user)
            print(request.user.groups.get())
            print(request.POST)
            print("-------------")
            print(request.FILES['file'])
            print("***************************")
            print("###############")
            form.save()
            return redirect('/admin')

    else:
        form = DocumentForm(user=None)

    print(Document.objects.all())
    return render(request, 'upload_doc.html', {'form': form})
