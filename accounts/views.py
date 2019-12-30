from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView
from django.forms.utils import ErrorList
from django import forms
from django.utils.http import is_safe_url

from .forms import LoginForm, RegisterForm


# class LoginView(FormView):
#     form_class = LoginForm
#     success_url = "/"
#     template_name = "accounts/login.html"

#     def form_valid(self, form):
#         request = self.request
#         email  = form.cleaned_data.get("email")
#         password  = form.cleaned_data.get("password")
#         user = authenticate(request=request, email=email, password=password)
#         print(user)
#         next_ = request.GET.get('next')
#         next_post = request.POST.get('next')
#         redirect_path = next_ or next_post or None
#         if user is not None:
#             login(request, user)
#             if is_safe_url(redirect_path, request.get_host()):
#                 return redirect(redirect_path)
#             return redirect("/")
#         form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(['Email or password is incorrect!'])
#         return super(LoginView, self).form_invalid(form)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if not request.user.is_authenticated:
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, email=email, password=password)
            next_ = request.GET.get('next')
            next_post = request.POST.get('next')
            redirect_path = next_ or next_post or None
            if user is not None:
                login(request, user)
                if is_safe_url(redirect_path, request.get_host()):
                    return redirect(redirect_path)
                return redirect('home')
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(['Email or password is incorrect!'])
        return render(request, "accounts/login.html", context)
    return redirect('home')


# class RegisterView(CreateView):
#     form_class = RegisterForm
#     template_name = "accounts/register.html"
#     success_url = "/login/"

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if not request.user.is_authenticated:
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        return redirect("home")

    return render(request, "accounts/register.html", context)
