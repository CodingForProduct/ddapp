
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from ddapp.core.forms import SignUpForm
from django.shortcuts import render, redirect
# from googlemaps import convert


@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db() 
            username = form.cleaned_data.get('username')
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def navigationview(request):
    return render(request, 'navigation.html')  
