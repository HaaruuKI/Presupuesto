from django.urls import path
from edit_account import views

urlpatterns = [
    path('editar_cuenta/<int:id_account>', views.edit_account, name='editar_cuenta'),
]
