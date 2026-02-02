from django import forms
from .models import ProductItems

class ItemForm(forms.ModelForm):  
  class Meta:
    model = ProductItems
    fields = ('category', 'item_image', 'item_title', 'item_discription')
    widgets = {
      'category': forms.Select(attrs={
        'class': 'border-2 border-blue-400 w-full py-1 rounded',
      }),
      'item_image': forms.FileInput(attrs={
        'class': 'border-2 border-blue-400 w-full py-1 rounded',
      }),
      'item_title': forms.TextInput(attrs={
        'class': 'border-2 border-blue-400 w-full py-1 rounded',
      }),
      'item_discription': forms.Textarea(attrs={
        'class': 'border-2 border-blue-400 w-full py-1 rounded',
      })
    }