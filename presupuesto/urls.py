from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('index/', include("main.urls")),
    path('',include("add_expenses.urls")),
    path('',include("view_expenses.urls")),
    path('',include("edit_expenses.urls")),
    # path('',include("add_accounts.urls")),
    # path('',include("add_categories.urls")),
    # path('',include("trasacciones.urls")),
    # path('',include("delete_transaction.urls")),
    # path('',include("edit_transaction.urls")),
    # path('',include("edit_account.urls")),
]
