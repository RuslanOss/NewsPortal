from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from news.models import Author

def signup_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            Author.objects.create(authorUser=user)
            login(request,user)
            return redirect('home')
    else: form=UserCreationForm()
    return render(request,'sign/signup.html',{'form':form})

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user(); login(request,user); return redirect('home')
    else: form=AuthenticationForm()
    return render(request,'sign/login.html',{'form':form})

@login_required
def profile_view(request):
    return render(request,'sign/profile.html',{'user':request.user})
