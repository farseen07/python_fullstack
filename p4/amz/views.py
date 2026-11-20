from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, "accounts/login.html", {
                'error': "invalid username or password"
            })

    return render(request, 'accounts/login.html')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def logout_page(request):
    logout(request)
    return redirect('login')