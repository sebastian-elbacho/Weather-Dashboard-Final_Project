from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView



app_name = "accounts"

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="accounts:login"), name="accounts_home"),
    path('register/', views.register, name='register'),
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html", extra_context={"body_class": "bg-auth"}), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("logged-out/", views.logged_out, name="logged_out"),
    



]
