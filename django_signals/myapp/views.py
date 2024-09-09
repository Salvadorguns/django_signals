from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db import IntegrityError
from .rectangle import Rectangle


def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if the user already exists
        if User.objects.filter(username=username).exists():
            return HttpResponse(f"User {username} already exists!")
        
        try:
            # Create a new user
            user = User.objects.create_user(username=username, password=password)
            return HttpResponse(f"User {user.username} created successfully!")
        except IntegrityError:
            return HttpResponse(f"Failed to create user {username} due to a unique constraint error.")
    
    return render(request, 'create_user.html')

def rectangle_view(request):
    # Create a Rectangle instance
    rectangle = Rectangle(length=10, width=5)
    context = {
        'length': rectangle.length,
        'width': rectangle.width
    }
    return render(request, 'rectangle.html', context)

def index(request):
    return render(request, 'index.html')