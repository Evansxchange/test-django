from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

from . import forms

# Create your views here.

def home(request):
 return render(request, "home.html")

@login_required()
def customer_page(request):
 return render(request, "customer_page.html")

@login_required()
def courier_page(request):
 return render(request, "courier_page.html")

def login(request):
 return render(request, "login.html")

def sign_up(request):
 form = forms.SignUpForm()

 if request.method == 'POST':
  form = forms.SignUpForm(request.POST)

  if form.is_valid():
   email = form.cleaned_data.get('email').lower()

   user = form.save(commit=False)
   user.username = email
   user.save()

   auth_login(request, user)
   return redirect('/')

 return render(request, 'sign_up.html',{'form' : form})
