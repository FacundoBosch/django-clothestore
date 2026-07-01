from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect
from django.contrib import messages

# decorator que chequea si el user está loggeado o no. En caso de que lo esté, redirije la vista
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        # lógica acá

        if request.user.is_authenticated:
            messages.info(request, f'¡Ya tienes una sesión iniciada!')
            return redirect('open:landing_page')
        else:
            return view_func(request, *args, **kwargs) # vista original

    return wrapper_func

# decorator que además recibe una serie de parámetros. Permitirá el acceso a solo los usuarios de que pertenezcan a allowed_roles
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            # lógica acá

            flag = False
            group = None
            if request.user.groups.exists(): # si el user pertenece a algun grupo
                for g in request.user.groups.all(): # recuperamos el nombre de todos los grupos
                    group.append(g.name)

            for item in allowed_roles:

                if item in group: # si el user pertenece a un grupo de allow_roles pasa
                    flag = True
                    return view_func(request, *args, **kwargs)

            if flag == False:
                return HttpResponseForbidden('no ta permitido weon')
        
        return wrapper_func
    return decorator

# decorator que solamente permite el acceso a los admins
def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):

        if request.user.groups.exists():

            if request.user.is_admin():
                return view_func(request, *args, **kwargs)
            else:
                messages.info(request, '¡No tienes permiso para acceder!')
                return redirect('open:landing_page')
        
    return wrapper_func
