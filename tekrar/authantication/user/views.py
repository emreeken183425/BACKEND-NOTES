from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required #(istediğimiz kişilerin görmesi için kısıtlama)

def home(request):
    return render(request,'user/home.html')

@login_required  # istediğimiz kişilerin görmesi için kısıtlama
def special(request):
    return render(request,"user/special.html")



def register(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            #buraya kadarki işlemler register için yeterli
            #bundan sonraki regiter olur olmaz login olması için 
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password1")
            user=authenticate(username=username,password=password)
            login(request,user)

            return redirect("home") 

    context={
        "form":form
    }
    return render(request,"registration/register.html",context)
