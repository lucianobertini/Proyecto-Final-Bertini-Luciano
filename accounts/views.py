from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from .models import Profile



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            profiles = Profile.objects.all()
            return render(request, 'accounts/profile_list.html', {'profiles': profiles})
    else:
        form = ProfileUpdateForm(instance=profile)
    
    return render(request, 'accounts/profile.html', {'form': form})



def profile_view(request):
    return render(request, 'blog/profile.html')

def edit_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            print("Perfil editado correctamente")  
            return redirect('profile_list')  
    else:
        form = ProfileUpdateForm(instance=profile)
    
    return render(request, 'accounts/edit_profile.html', {'form': form})

@login_required
def profile_list(request):
    profiles = Profile.objects.all() 
    return render(request, 'accounts/profile_list.html', {'profiles': profiles})


def profile_detail(request, user_id):
    profile = get_object_or_404(Profile, user__id=user_id)
    return render(request, 'accounts/profile_detail.html', {'profile': profile})

@login_required
def user_profile(request):
    profile = request.user.profile 
    return render(request, 'accounts/user_profile.html', {'profile': profile})