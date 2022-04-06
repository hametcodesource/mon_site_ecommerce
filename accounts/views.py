from unittest import result
from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .forms import UserForm

def register(request):
    if request.user.is_active:
       return redirect("shop:product_list")
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:login")
    else:
        form=UserForm()

    return render(request,"accounts/register.html",{'form':form})