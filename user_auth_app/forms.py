from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustemUserForm(UserCreationForm):
  USER_SEX_MALE = 'M'
  USER_SEX_FEMALE = 'F'
  USER_SEX_NONE = 'N'
  USER_SEX_CHOICES = [
    (USER_SEX_NONE, 'None'),
    (USER_SEX_MALE, 'Male'),
    (USER_SEX_FEMALE, 'Female'),
  ]
  sex = forms.ChoiceField(choices=USER_SEX_CHOICES, initial=USER_SEX_NONE)
  class Meta: 
    model = User 
    fields = ('username', 'email', 'sex')
    widgets = {
      'username': forms.TextInput(attrs={
        'class': 'border-2 border-blue-400 w-full py-1 rounded',
      }),
      'email': forms.TextInput(attrs={
        'class': 'border-2 border-blue-400 w-full py-1 rounded',
      }),
      'password1': forms.PasswordInput(attrs={
        'class': 'border-2 border-blue-400 mx-20',
      }),
    }