from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator

# para controlar que un user esté loggeado
from django.contrib.auth.decorators import login_required
# decorator personalizado para restringir acceso a usuarios de X roles / grupos
from users.decorators import allowed_users, admin_only

from .models import Categoria, Ropa
from .forms import categoriaForm, ropaForm

#@allowed_users(allowed_roles=['admins']) # se pone debajo del login_required, y se pasa en el array el nombre de/los grupo/s 
@login_required(login_url='user:user_login') # poner esto arriba de cada view restringida
@admin_only
def main_panel(request):
    return render(request, 'products/mainPanel.html')

### COMIENZA LA SECCIÓN DE CATEGORIAS

@login_required(login_url='user:user_login')
@admin_only
def panel_categorias(request):

    categorias = Categoria.objects.all().order_by('name')
    
    # trae el valor de q, y si no existe trae null
    filter = request.GET.get('q', '')
    
    # para display una cantidad x de elementos por página
    elemsPorPagina = 10
    paginator = Paginator(categorias, elemsPorPagina)
    pagActual = request.GET.get('page', 1)
    
    elemsPaginaActual = paginator.get_page(pagActual) # este es el que tiene todas las categorias de la pag actual

    if filter:
        # poner name__icontains es como poner name LIKE %value%
        elemsPaginaActual = categorias.filter(name__icontains=filter) 

    # obtener todos los fields, menos los derivados de las relaciones
    attributes = [field.name for field in Categoria._meta.get_fields() if not (field.is_relation and field.auto_created)]
    return render(request, 'products/categorias/mainCategorias.html', {'categorias': elemsPaginaActual, 'keys': attributes, 'filtro': filter})

@login_required(login_url='user:user_login')
@admin_only
def panel_categorias_add(request):

    type = 'Agregar'

    if request.method == "POST":

        form = categoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save()
            return redirect('management:panel_categorias')
    else:

        form = categoriaForm()
        return render(request, 'products/categorias/addeditCategorias.html', {'form': form, 'type': type})

@login_required(login_url='user:user_login')
@admin_only
def panel_categorias_edit(request, cid):

    type = 'Editar'
    categoria = Categoria.objects.filter(id = cid).first()

    if request.method == 'POST':

        form = categoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            categoria = form.save()
            return redirect('management:panel_categorias')

    else:

        form = categoriaForm(instance=categoria)
        return render(request, 'products/categorias/addeditCategorias.html', {'form': form, 'type': type})

### TERMINA LA SECCIÓN DE CATEGORIAS
### COMIENZA LA SECCIÓN DE ROPAS

@login_required(login_url='user:user_login')
@admin_only
def panel_ropas(request):

    ropas = Ropa.objects.all().order_by('id')
    
    # trae el valor de q, y si no existe trae null
    filter = request.GET.get('q', '')
    
    # para display una cantidad x de elementos por página
    elemsPorPagina = 15
    paginator = Paginator(ropas, elemsPorPagina)
    pagActual = request.GET.get('page', 1)
    
    elemsPaginaActual = paginator.get_page(pagActual) # este es el que tiene todas las ropas de la pag actual

    if filter:
        # poner name__icontains es como poner name LIKE %value%
        elemsPaginaActual = ropas.filter(name__icontains=filter) 

    # obtener todos los fields, menos los derivados de las relaciones
    attributes = [field.name for field in Ropa._meta.get_fields() if not (field.is_relation and field.auto_created)]
    return render(request, 'products/ropas/mainRopas.html', {'ropas': elemsPaginaActual, 'keys': attributes, 'filtro': filter})

@login_required(login_url='user:user_login')
@admin_only
def panel_ropas_add(request):

    type = 'Agregar'

    if request.method == "POST":

        form = ropaForm(request.POST, request.FILES)
        if form.is_valid():
            ropa = form.save()
            return redirect('management:panel_ropas')
    else:

        form = ropaForm()
        return render(request, 'products/ropas/addeditRopas.html', {'form': form, 'type': type})

@login_required(login_url='user:user_login')
@admin_only
def panel_ropas_edit(request, rid):

    type = 'Editar'
    ropa = Ropa.objects.filter(id = rid).first()

    if request.method == 'POST':

        form = ropaForm(request.POST, request.FILES, instance=ropa)
        if form.is_valid():
            ropa = form.save()
            return redirect('management:panel_ropas')

    else:

        form = ropaForm(instance=ropa)
        return render(request, 'products/ropas/addeditRopas.html', {'form': form, 'type': type})

@login_required(login_url='user:user_login')
@admin_only
def panel_ropas_imagen(request, rid):

    ropa = Ropa.objects.filter(id = rid).first()
    return render(request, 'products/ropas/fotoRopa.html', {'ropa': ropa})