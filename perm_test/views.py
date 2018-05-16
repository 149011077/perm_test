from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

def index(request):
    if request.method == 'GET':
        username = request.user.username
        return render(request, "index.html", {'username':username})

def acc_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username)
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            # print("Yes")
            # return redirect('/get_classes.html')
            # next_url = request.GET['next']
            next_url = request.GET.get('next')
            if next_url:
                return HttpResponseRedirect(next_url)
            else:
                return redirect('/index/')
        # print("No")
    return render(request, "login.html")


def acc_logout(request):
    logout(request)
    return redirect("/login")