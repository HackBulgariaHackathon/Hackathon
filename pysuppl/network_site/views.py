from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def index(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

    return render(request, 'network_site/index.html', locals())
