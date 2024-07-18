from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('',include("add_accounts.urls")),
    path('',include("add_categories.urls")),
    path('',include("trasacciones.urls")),
    path('',include("payments.urls")),
    path('',include("delete_transaction.urls")),
    path('',include("edit_transaction.urls")),
]
