from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .models import *


@login_required(login_url="network:login")
def index(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username

    return render(request, 'network_site/index.html', locals())


@login_required
def site_logout(request):
    auth_views.logout(request)
    return redirect('network:index')


def site_login(request):
    if request.user.is_authenticated():
        return redirect("network:index")
    else:
        return auth_views.login(request, template_name='network_site/signin.html')


def get_networks(request):
    networks = Network.objects.all()
    # print(networks)
    return render(request, "get_networks.html", locals())
