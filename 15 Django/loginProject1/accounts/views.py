from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('home')   # redirect to home page successfully.
        else:
            messages.error(request, 'Invalid username or password.')
            
    return render(request, 'accounts/login.html')

