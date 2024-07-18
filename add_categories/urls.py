from django.urls import path
from add_categories import views

urlpatterns = [
    path('agregar_categoria/', views.add_category, name='agregar_categoria'),
]
