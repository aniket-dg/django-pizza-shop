from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('order.urls')),
    path('', include('order.urls')),
    path('api/', include('api.urls')),



]
