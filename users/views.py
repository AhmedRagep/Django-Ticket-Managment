from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import RegisterCustomerForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterCustomerForm(data=request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            # لتعريف اليوزر الجديد بانه يوزر وليس مهندس
            var.customer = True
            var.save()
            messages.info(request, 'You Accounts has been successfully please login to conuenue')
            return redirect('login')
        else:
            messages.warning(request, 'Somsing went warong please chack form')
            return redirect('register')
    else:
        form = RegisterCustomerForm()
        return render(request, 'register.html', {'form':form})
    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            auth_login(request, user)
            messages.info(request,'login successfully please enjoy!')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Somsing went warong please chack form')
            return redirect('login')
    else:
        return render(request, 'login.html')
        

def logout(request):
    auth_logout(request)
    messages.info(request, 'You sesson has ended , login to contenue')
    return redirect('login')