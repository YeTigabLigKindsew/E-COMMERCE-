from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
from .forms import ItemForm


@staff_member_required
def item_form(request):
  if request.method == "POST":
    form = ItemForm(request.POST, request.FILES)
    if form.is_valid():  
      form.save()
      return redirect('auth:home')
      
  else:
    form = ItemForm()
  return render(request, 'upload.html', {'form': form})
