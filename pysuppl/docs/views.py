from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
# Create your views here.
from django.contrib.auth import models
from django.conf import settings




@login_required(login_url='/login')
def index(request):
    current_user = request.user
    group = current_user.groups.get()
    users = group.user_set.all()
    prefix = settings.MEDIA_URL
    # user = users[0]
    documents = []
    for user in users:
        documents += Document.objects.filter(uploader=user.id)

    return render(request, 'docs.html', locals())


@login_required(login_url='/login')
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
            return redirect('/docs/index')

    else:
        form = DocumentForm(user=None)

    print(Document.objects.all())
    return render(request, 'upload_doc.html', {'form': form})
