from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from accounts.forms import LoginForm, SignUpForm


class SignUpView(CreateView):
    template_name = "accounts/inc/register.html"
    form_class = SignUpForm
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    template_name = "accounts/inc/login.html"
    authentication_form = LoginForm
    next_page = 'index'


class CustomLogoutView(LogoutView):
    next_page = 'index'
