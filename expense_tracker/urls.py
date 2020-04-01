"""expense_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from expense.views import signup, signin, signout, dashboard, get_all_wallet, get_all_expense, get_all_income, create_wallet, create_expense, create_income, delete_wallet, delete_expense, delete_income, edit_wallet, edit_expense, edit_income
urlpatterns = [
    path('admin/', admin.site.urls),
    path("signup/", signup),
    path("signin/", signin),
    path("signout/", signout),
    path("dashboard/", dashboard),
    path("wallet/", get_all_wallet),
    path("expense/", get_all_expense),
    path("income/", get_all_income),
    path("create_wallet/", create_wallet),
    path("create_expense/", create_expense),
    path("create_income/", create_income),
    path("delete_wallet/<int:wallet_id>/", delete_wallet),
    path("delete_expense/<int:expense_id>/", delete_expense),
    path("delete_income/<int:income_id>/", delete_income),
    path("edit_wallet/<int:wallet_id>/", edit_wallet),
    path("edit_expense/<int:expense_id>/", edit_expense),
    path("edit_income/<int:income_id>/", edit_income),
]
