from django import forms
from .models import Categoria, Ropa

class categoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ['name', 'active']

class ropaForm(forms.ModelForm):

    class Meta:
        model = Ropa
        fields = ['name', 'desc', 'categoria', 'stock', 'price', 'img', 'active']
    
    # Sobreescribimos el constructor del formulario
    def __init__(self, *args, **kwargs):
        # Esto es para dejar que se arme normalmente
        super(ropaForm, self).__init__(*args, **kwargs)
        
        # Le aplicamos el filtro al queryset del campo 'categoria'
        # Solo va a listar las que tengan active=True
        self.fields['categoria'].queryset = Categoria.objects.filter(active=True)