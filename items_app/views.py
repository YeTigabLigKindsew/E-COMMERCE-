from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
from .forms import ItemForm


@user_passes_test(lambda u: u.is_superuser)
def item_form(request):
  if request.method == "POST":
    form = ItemForm(request.POST, request.FILES)
    if form.is_valid():  
      form.save()
      return redirect('auth:home')
      
  else:
    form = ItemForm()
  return render(request, 'upload.html', {'form': form})
