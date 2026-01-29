from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        label="Name",
        widget=forms.TextInput(
            attrs={
                "class": "w-full border rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500",
                "placeholder": "Name",
            }
        ),
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "w-full border rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500",
                "placeholder": "Email",
            }
        )
    )

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
        fields = ("first_name", "email", "username", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already in use.")
        return email
