from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q

from products.models import Ropa, Categoria

def landing_page(request):

    categorias = Categoria.objects.filter(active = True).order_by('name')
    ropas = Ropa.objects.filter(active = True).order_by('name')

    ## FILTROS
    filterCat = request.GET.get('cat', '')
    filterprice = request.GET.get('price', '')
    
    if filterprice:
        # los rangos de precio se obtienen directamente del html
        pricerange = filterprice.split('-', 2)
        
        if pricerange[0] == '0':
            # para incluir una clausula OR en el filter, se debe usar la Q y en medio el separador |
            ropas = ropas.filter(Q(price__lte = float(pricerange[1])) | Q(price__isnull = True))
        elif pricerange[1] == 'x':
            ropas = ropas.filter(price__gte = float(pricerange[0]))
        else:
            # atributo__gte significa greater than or equal, atributo__lte significa less than or equal
            ropas = ropas.filter(price__gte = float(pricerange[0]), price__lte = float(pricerange[1]))

    if filterCat:
        ropas = ropas.filter(categoria = filterCat)



    ## PAGINACIÓN
    elemsPorPagina = 6
    paginator = Paginator(ropas, elemsPorPagina)
    pagActual = request.GET.get('page', 1)
    elemsPaginaActual = paginator.get_page(pagActual)

    return render(request, 'open_websites/landingPage.html', {
        'ropas': elemsPaginaActual, 
        'cats': categorias,

        'filtercat': filterCat,
        'filterprice': filterprice
        })