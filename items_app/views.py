from django.shortcuts import render, redirect

# Create your views here.
from .forms import ItemForm

def item_form(request):
  if request.method == "POST":
    form = ItemForm(request.POST, request.FILES)
    if form.is_valid():  
      form.save()
      return redirect('auth:home')
      
  else:
    form = ItemForm()
  return render(request, 'upload.html', {'form': form})