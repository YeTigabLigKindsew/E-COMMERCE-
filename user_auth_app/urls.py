from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views 

app_name = "auth"

urlpatterns = [
  path('', views.home, name="home"),
  path('signup/', views.user_signup, name="signup"),
  path('login/', views.user_login, name="login"),
  path('logout/', views.user_logout, name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)