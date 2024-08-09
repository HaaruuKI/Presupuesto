from django.urls import path
from delete_transaction import views

urlpatterns = [
    path('borrar_transaccion/<int:id_trasaction>/', views.delete_transaction, name="borrar_transaccion")
]
