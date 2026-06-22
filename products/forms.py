from django import forms
from .models import Categoria, Ropa

class categoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ['name', 'active']

class ropaForm(forms.ModelForm):

    class Meta:
        model = Ropa
        fields = ['name', 'desc', 'categoria', 'stock', 'price', 'active']