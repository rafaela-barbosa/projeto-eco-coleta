from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('materiais/', views.materiais, name='materiais'),
    path('como-funciona/', views.como_funciona, name='como_funciona'),
    path('mapa/', views.mapa, name='mapa'),
    path('contato/', views.contato, name='contato'),
]