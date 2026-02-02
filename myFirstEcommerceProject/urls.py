
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_auth_app.urls')),
    path('items/', include('items_app.urls')),
    path('detail/', include('detailapp.urls')),
]
