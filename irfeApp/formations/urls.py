
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
   
    path('', views.formation_view, name='formations'),
    path('form', views.load_form, name='ajout_formation'),
    path('add_formation', views.add_formation),
    path('detail_formation/<int:id>', views.detail_formation)
]
