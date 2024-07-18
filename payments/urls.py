from django.urls import path
from payments import views

urlpatterns = [
    path('payment/', views.payments, name='payment'),
]
