from django.urls import path
from view_expenses import views

urlpatterns = [
    path('ViewExpenses/', views.view_expenses, name='view_expenses'),
]
