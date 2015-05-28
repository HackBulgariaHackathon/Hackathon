from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
# Create your views here.
from django.contrib.auth import models




#@login_required
def index(request):
    current_user = request.user
    group = current_user.groups.get()
    # group = request.user.groups.get()
    print(group)

    users = group.user_set.all()
    print(users)
    # documents = [Document.objects.filter(uploader=uploader.id) for uploader in users]
    # documents = []
    # for user in users:
    user = users[0]
    documents = Document.objects.get(uploader=user.id)

    print("Index")
    print(documents)
    return render(request, 'docs.html', locals())


@login_required
def upload(request):

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, user=request.user)
        # user = request.user.id
        # gr = user.groups.all()
        # print("USER: {}".format(users))
        if form.is_valid():
            print("###############")
            print(request.user)
            # print(Group.objects.get(grp).user_set.all())
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
