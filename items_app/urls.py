from django.urls import path

from .views import item_form
app_name = "items"
urlpatterns = [
  path('upload/', item_form, name="form"),
]