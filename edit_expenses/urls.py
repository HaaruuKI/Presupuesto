from django.urls import path
from edit_expenses import views

urlpatterns = [
    path('EditExpenses/<int:id_expenses>', views.edit_expenses, name="edit_expenses")
]
