from django.shortcuts import render, redirect
# formulario pre-creado para el register de users
from django.contrib.auth.forms import UserCreationForm
# formulario de antes pero modificado desde mi formspy
from .forms import CreateUserForm

# otras cosas pre-creadas utiles para el manejo de usuarios
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import Group

# decoradores personalizados
from .decorators import unauthenticated_user

# para controlar que un user esté loggeado antes de acceder a una pag. mirar en products views

@unauthenticated_user
def register_view(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
            
        if form.is_valid():
            user = form.save()

            # cuando un user se registra, se asocia automáticamente con el grupo 'users'
            group = Group.objects.get(name='users')
            user.groups.add(group)

            username = form.cleaned_data.get('username')
            messages.success(request, f'Usuario {username} creado! Ahora loggeate pelotudo')
            return redirect('user:user_login')

    return render(request, 'users/register.html', {'form': form})

@unauthenticated_user
def login_view(request):

    if request.method == 'POST':
        # recuperando los datos del form de login
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None: # si el usuario existe en la db, loggeamos
            login(request, user)
            return redirect('open:landing_page')
            
        else: # sino, mandamos msg de incorrecto y lo devolvemos a la pag donde estaba
            messages.info(request, 'Username or password is incorrect')

    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('open:landing_page')