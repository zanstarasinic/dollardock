"""
URL configuration for dollardock project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/login/', obtain_auth_token, name='api-login'),
    path('api/auth/logout/', views.logout_view, name='api-logout'),
    path('api/register/', views.register_view, name='register'),
    path('api/account/', views.get_user_account, name='account-list'),
    path('api/account/<int:account_id>/transactions/', views.get_account_transactions, name='account-transactions'),
    path('api/account/<int:account_id>/transactions/create', views.create_transaction, name='add-account-transaction'),
    path('api/account/<int:account_id>/transactions/<int:transaction_id>/delete/', views.delete_transaction, name='delete-transaction'),
    path('api/account/<int:account_id>/transactions/<int:transaction_id>/edit/', views.edit_transaction, name='edit-transaction'),


]
