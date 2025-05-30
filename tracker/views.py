from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Transaction
from django.db.models import Sum
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import time
import logging
logger = logging.getLogger(__name__)
# Create your views here.

def registration(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(Q(username=username)| Q(email=email))
        if user_obj.exists():
            messages.error(request, 'User already exists')
            return redirect('registration')
         
        user_obj = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
        )
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request, 'User created successfully')
        return redirect('registration')
        
    return render(request, 'registration.html',)

@login_required(login_url='login_page')
def index(request):
    time.sleep(1)
    print(request.user)
    if request.method == 'POST':
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        if description == '' or amount == '':
            messages.error(request, 'Please fill all the fields')
            return render(request, 'index.html',)
        try:
            obj = Transaction.objects.create(description=description, amount=amount, created_by=request.user)
            obj.save()
            messages.info(request, 'Transaction added successfully')
            return redirect('index')

        except Exception as e:
            print(e)
        
       
        
    context = {"transactions":Transaction.objects.filter(created_by=request.user).order_by('-created_at'),
               'balance':Transaction.objects.filter(created_by=request.user).aggregate(total_sum = Sum('amount')),
               'income':Transaction.objects.filter(created_by=request.user,amount__gte = 0).aggregate(income = Sum('amount'))['income'] or 0,
               'expense':Transaction.objects.filter(created_by=request.user,amount__lt=0).aggregate(expense = Sum('amount'))['expense'] or 0}
    
    return render(request, 'index.html', context)


def login_page(request):
    logger.debug('this is debug message')
    logger.info('this is info message')
    logger.warning('this is warning message')
    logger.error('this is error message')
    logger.critical('this is critical message')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.error(request, 'User does not exist')
            return redirect('login_page')
        
        user_obj = authenticate(username=username,password=password)
        if not user_obj:
            messages.error(request, 'Invalid credentials')
            return redirect('login_page') 
        login(request,user_obj)
        messages.info(request, 'Login successful')
        return redirect('index')    
    return render(request, 'login.html',)

def logout_page(request):
    logout(request)
    messages.info(request, 'Logout successful')
    return redirect('login_page') 


def deletetransaction(request,uuid):
    Transaction.objects.get(uuid=uuid).delete()
    return redirect('index')