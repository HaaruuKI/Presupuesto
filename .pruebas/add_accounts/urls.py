from django.urls import path
from add_accounts import views

urlpatterns = [
    path('agregar_cuenta/', views.add_accounts, name="agregar_cuenta"),
]
