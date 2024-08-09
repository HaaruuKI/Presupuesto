from django.urls import path
from main import views

urlpatterns = [
    path('', views.main, name="main"),
    path('logout_account/', views.logout_view, name='logout_account'),

]
