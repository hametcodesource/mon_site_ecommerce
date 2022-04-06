from dataclasses import field, fields
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username=forms.CharField(label="Usernam",widget=forms.TextInput(attrs={
        'color':'red','class':'form-control'
    }))

    password=forms.CharField(label="password",widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }))


class UserForm(UserCreationForm):
    username=forms.CharField(label="Usernam",widget=forms.TextInput(attrs={
        'class':'form-control'
    }))

    email=forms.CharField(label="email",widget=forms.EmailInput(attrs={
        'class':'form-control'
    }))


    password1=forms.CharField(label="password",widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }))
    password2=forms.CharField(label="confirm password",widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }))   
    class Meta:
        model=User
        fields=('username','email','password1','password2')