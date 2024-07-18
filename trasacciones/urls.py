from django.urls import path
from trasacciones import views

urlpatterns = [
    path('trasacciones/', views.trasacciones, name='trasacciones'),
]
