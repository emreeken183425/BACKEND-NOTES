from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login






def home(request):
    return render(request, 'user_example/index.html')

def special(request):
    return render(request, "user_example/special.html")

def register(request):
    # kısa yol
    form = UserCreationForm(request.POST or None)
    # form = UserCreationForm()burası uzun olanı
    # if request.method=='POST':yukardaki kısa olanı 
    #     form=UserCreationForm(request.POST)
    
    if form.is_valid():
        form.save()
          # that creates a new user
            # after creation of the user, want to authenticate it
        username = form.cleaned_data.get['username']
        password = form.cleaned_data.get['password1']
            # inspect the page and see the first password is password1, import authenticate
        user = authenticate(username=username, password=password)
            
            # want user to login right after registered, import login
        login(request, user)
            # want to redirect to home page, import redirect
        return redirect('home')
        
    
    context = {
        'form': form
    }
    return render(request, "registration/register.html", context)

def password_change(request):
    if request.method == 'POST':
        # We will use user change form this time
        # Import it
        form = UserChangeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = UserChangeForm()
    
    context = {
        'form': form
    }
    
    return render(request, "registration/password_change.html", context)    