from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formulario/', views.formulario_encomienda, name='formulario_encomienda'),
    path('confirmacion/', views.confirmacion, name='confirmacion'),
]
