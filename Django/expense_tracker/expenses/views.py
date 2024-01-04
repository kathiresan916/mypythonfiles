from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm

# Create your views here.


def expence_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expense/expense_list.html', {'expenses': expenses})


def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
        else:
            form = ExpenseForm()
        return render(request, 'expenses/add_expense.html', {'form': form})
