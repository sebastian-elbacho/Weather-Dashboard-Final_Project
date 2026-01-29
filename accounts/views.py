from django.shortcuts import render, redirect
from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:login")
    else:
        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form, "body_class": "bg-auth"},
    )


def logged_out(request):
    return render(request, "accounts/logged_out.html", {"body_class": "bg-auth"})
