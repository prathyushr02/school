# credentials/views.py
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'credentials/home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Correct method is auth.authenticate, not auth.authentication
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('credentials:formpage')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('credentials:login')

    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']  # Correct variable name
        password2 = request.POST['password2']  # Correct variable name

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('credentials:register')
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                return redirect('credentials:login')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('credentials:register')

    return render(request, "register.html")


def formpage(request):
    confirmation_message = None

    if request.method == 'POST':
        # Process the form data (handle form submission logic here)
        confirmation_message = 'Order Confirmed'  # You can customize this message
        print("Confirmation Message:", confirmation_message)  # Add this line for debugging
        return render(request, 'formpage.html', {'confirmation_message': confirmation_message})

    return render(request, 'formpage.html', {'confirmation_message': confirmation_message})
