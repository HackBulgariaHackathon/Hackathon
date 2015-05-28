from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden
from django.contrib.auth.decorators import login_required

from .models import Wiki

# Create your views here.


def show_wiki(request):
    wiki = Wiki.objects.all()
    return render(request, 'show_wiki.html', locals())

def show_text(request, wiki_id):
    #wiki_id = request.GET.get("wiki_id")
    wik = get_object_or_404(Wiki, pk=wiki_id)
    current_user = request.user
    txt = Wiki.objects.filter(title=wik.title)
    return render(request, 'show_text.html', locals())


@login_required
def edit_text(request):
    pass
