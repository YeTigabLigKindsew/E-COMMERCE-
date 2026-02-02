from django.shortcuts import render, get_object_or_404

from items_app.models import ProductItems
# Create your views here.
def item_detail(request, id):
  item = get_object_or_404(ProductItems ,pk=id)
  related = ProductItems.objects.filter(category=item.category, item_is_sold=False).exclude(pk=id)
  return render(request, 'detail.html', {'item':item, "relates":related})