from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Transaction
from django.db.models import Sum
# Create your views here.


def index(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        if description == '' or amount == '':
            messages.error(request, 'Please fill all the fields')
            return render(request, 'index.html',)
        try:
            obj = Transaction.objects.create(description=description, amount=amount)
            obj.save()
            messages.info(request, 'Transaction added successfully')
            return redirect('index')

        except Exception as e:
            print(e)
        
       
        
    context = {"transactions":Transaction.objects.all().order_by('-created_at'),
               'balance':Transaction.objects.all().aggregate(total_sum = Sum('amount')),
               'income':Transaction.objects.filter(amount__gte = 0).aggregate(income = Sum('amount'))['income'] or 0,
               'expense':Transaction.objects.filter(amount__lt=0).aggregate(expense = Sum('amount'))['expense'] or 0}
    return render(request, 'index.html', context)


def deletetransaction(request,uuid):
    Transaction.objects.get(uuid=uuid).delete()
    return redirect('/tracker/')