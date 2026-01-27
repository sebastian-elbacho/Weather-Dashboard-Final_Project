from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full border rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500",
                "placeholder": "Username",
            }
        )
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full border rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500",
                "placeholder": "Password",
            }
        ),
    )

    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full border rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500",
                "placeholder": "Confirm password",
            }
        ),
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2")
