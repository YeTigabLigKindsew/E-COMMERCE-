from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()
# Create your models here.
class ProductType(models.Model):
  type_of_items = models.CharField(max_length=100)
  
  def __str__(self):
    return self.type_of_items
  
class ProductItems(models.Model):
  category = models.ForeignKey(ProductType, related_name="items", on_delete=models.CASCADE)
  item_image = models.ImageField(upload_to="items_photo")
  item_title = models.CharField(max_length=100)
  item_discription = models.TextField(blank=True, null=True)
  item_added_time = models.DateTimeField(auto_now_add=True)
  item_is_sold = models.BooleanField(default=False)
  
  def __str__(self):
    return f"{self.item_title}"