from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirige a la página de bienvenida (puedes cambiar 'welcome' por la URL que prefieras).
            return redirect('welcome')
        else:
            # Handle authentication error if needed
            pass

    return render(request, 'login.html')

@login_required(login_url='login')  # Esto asegura que solo usuarios autenticados puedan acceder a esta vista
def welcome_view(request):
    return render(request, 'welcome.html')