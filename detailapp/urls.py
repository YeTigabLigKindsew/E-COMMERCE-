from django.urls import path
from . import views

app_name = "detail"

urlpatterns = [
  path('<int:id>/', views.item_detail, name='item'),
]