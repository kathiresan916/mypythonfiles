# expenses/urls.py

from django.urls import path
from .views import expence_list, add_expense

urlpatterns = [
    path('', expence_list, name='expense_list'),
    path('add/', add_expense, name='add_expense'),
]
