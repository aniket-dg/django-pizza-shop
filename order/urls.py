from django.urls import path
from .views import orderGenerate
urlpatterns = [
    path('', orderGenerate, name='order_generate'),
    path('order/placed', orderGenerate, name='order_generate'),
]