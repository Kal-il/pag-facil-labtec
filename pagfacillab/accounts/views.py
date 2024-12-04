import re
from django.shortcuts import render, redirect
from .admin import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views_dir here.
def register(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_valid = False
            user.save()
            messages.success(request, 'Registrado. Agora faça o login para começar!')
            return redirect('home')

        else:
            print('invalid registration details')
            
    return render(request, "registration/register.html",{"form": form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Bem Vindo (a) '+ user.first_name)
            return redirect('home')
        else:
            # Autenticação falhou, lide com isso de acordo
            messages.debug(request, 'Ops! Aconteceu algum erro.')
    # Renderize o formulário de login
    return render(request, 'registration/login.html')


def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    messages.success(request, 'Você saiu com sucesso.')
    return redirect('login')

def password_reset(request):
    # Add your logout logic here
    pass
