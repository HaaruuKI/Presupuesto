from django.urls import path
from edit_transaction import views

urlpatterns = [
    path('editar_transaccion/<int:id_transaction>', views.edit_transaction, name="editar_transaccion")
]
