from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login")
def index(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username

    return render(request, 'network_site/index.html', locals())


def site_logout(request):
    logout(request)
    return redirect("network:index")


def site_login(request):
    if request.user.is_authenticated():
        return redirect("network:index")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print (username, password)
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("network:index")
        else:
            return redirect("network:index")

    else:
        return render(request, 'network_site/signin.html', locals())
