from django.urls import path, include
from . import views

app_name = 'management'

urlpatterns = [
    path('', views.main_panel, name='main_panel'),
    path('categorias', views.panel_categorias, name='panel_categorias'),
    path('categorias/add', views.panel_categorias_add, name='panel_categorias_add'),
    path('categorias/editar/<int:cid>', views.panel_categorias_edit, name='panel_categorias_edit'),

    path('ropas', views.panel_ropas, name='panel_ropas'),
    path('ropas/add', views.panel_ropas_add, name='panel_ropas_add'),
    path('ropas/editar/<int:rid>', views.panel_ropas_edit, name='panel_ropas_edit'),
    path('ropas/imagen/<int:rid>', views.panel_ropas_imagen, name='panel_ropas_imagen'),
]