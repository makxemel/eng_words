from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = '__all__'


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        label='password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    password2 = forms.CharField(
        label='password confirmation',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control'}),
        #     'username': forms.PasswordInput(attrs={'class': 'form-control'}),
        #     'username': forms.PasswordInput(attrs={'class': 'form-control'}),
        # }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = User
        fields = ('username', 'password')
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control'}),
        #     'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        # }
