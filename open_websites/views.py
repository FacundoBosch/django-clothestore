from django.shortcuts import render
from django.http import HttpResponse

from products.models import Ropa

def landing_page(request):

    ropas = Ropa.objects.all()
    return render(request, 'open_websites/landingPage.html', {'ropas': ropas})