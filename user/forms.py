from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'username', 'placeholder': 'Username'}))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'required': True, 'id': 'password', 'placeholder': 'Password'}))
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'form-check-input', 'id': 'remember_me'}))


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Your Username', 'id': 'username'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Your Email', 'id': 'email'}),
            'password': forms.PasswordInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Your Password', 'id': 'password'}),
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'is_active')

        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Your First Name', 'id': 'first_name'}
            ),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Your Last Name', 'id': 'last_name'}
            ),
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Your Username', 'id': 'username'}
            ),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Your Email', 'id': 'email'}
            ),
            'is_active': forms.CheckboxInput(
                attrs={'class': 'form-check-input', 'id': 'is_active'}
            )
        }
