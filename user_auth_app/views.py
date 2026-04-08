from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CustemUserForm
from items_app.models import ProductItems, ProductType
# Create your views here.
def home(request):
  productType = ProductType.objects.all()
  
  context = {
    "productTypes": productType,
  }
  return render(request, 'home.html', context)
  
def user_signup(request):
  if request.method == "POST":
    form = CustemUserForm(request.POST)
    if form.is_valid():  
      user = form.save()
      login(request, user)
      return redirect('auth:home')
  else:
    form = CustemUserForm()
  return render(request, 'signup.html', {'form':form})
  
def user_login(request):
  if request.method == "POST":  
    Uname = request.POST.get('username')
    P = request.POST.get('password')
    user = authenticate(request, username=Uname, password=P)
    if user is not None:
      login(request, user)
      messages.success(request, "you login succesfuly.")
      return redirect('auth:home')
    else:
      messages.success(request, "Invalid please try again.")
      return redirect('auth:login')
  else:
    return render(request, 'login.html')

@login_required(login_url='login')  
def user_logout(request):
  logout(request)
  messages.success(request, "you succesfuly logout")
  return redirect('auth:login')

"""
only super user
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_action(request):
    ...

from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def admin_action(request):
    ...

"""
