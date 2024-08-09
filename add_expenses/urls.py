from django.urls import path
from add_expenses import views

urlpatterns = [
    path('expenses/', views.add_expenses, name='expenses'),
]
