from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('order.urls')),
    path('', include('order.urls')),
    path('api/', include('api.urls')),
    path('docs/', include_docs_urls(title = 'API Document')),



]
