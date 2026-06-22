from django.db import models

class Categoria(models.Model):
    name = models.CharField(max_length=50, null=False)
    active = models.BooleanField(default=True)

    def __str__(self):

        estado = ''
        if self.active:
            estado = 'Activa'
        else:
            estado = 'Inactiva'

        return f'{self.name} - {estado}'
    
class Ropa(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    desc = models.CharField(max_length=250, null=True, blank=True)
    stock = models.IntegerField(null=False, blank=True, default=0)
    price = models.FloatField(null=True, blank=True)
    img = models.ImageField(upload_to='ropa_fotos/', null=True, blank=True)
    active = models.BooleanField(default=True)

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='ropas', null=True, blank=False)

    def __str__(self):
        return f'{self.name}, UNIDADES: {self.stock} - {self.active}'
