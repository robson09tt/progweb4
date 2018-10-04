from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('json/exemplo', views.json_exemplo, name='json_exemplo'),  
    path('json/listartwips', views.json_listar_twips, name='json_listar_twips'),
]
