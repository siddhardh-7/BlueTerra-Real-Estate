from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

# Create your views here.
def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')
    # Login user
    username = request.POST['username']
    password = request.POST['password']
    
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        messages.success(request, 'You are now logged in')
        return redirect('dashboard')
    else:
        messages.error(request, 'Invalid credentials')
        return redirect('login')

def register(request):
    if request.method != 'POST':
        return render(request, 'accounts/register.html')
    password = request.POST['password']
    password2 = request.POST['password2']

        # check passwords match
    if password != password2:
        messages.error(request, 'Passwords do not match')
        return redirect('register')
    else:
        # Get Form Values
        username = request.POST['username']
        email = request.POST['email']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('register')
        else:
            # Looks good
            user = User.objects.create_user(username=username, password=password, email=email)
            # Login after register
            # auth.login(request, user)
            # messages.success(request, 'You are now logged in')
            # return redirect('index')
            user.save()
            messages.success(request, 'You are now registered and can log in')
            return redirect('login')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')

def dashboard(request):
    user_contacts = Contact.objects.filter(user_id=request.user.id).order_by('-contact_date')
    context = {
        'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)