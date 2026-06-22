from django.urls import path, include
from . import views

app_name = 'open'

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
]
