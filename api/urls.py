from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListOrder.as_view(), name='order_list'),
    path('order/list', views.ListOrder.as_view(), name='order_list'),
    path('order/create', views.CreateOrder.as_view(), name='order_create'),
    path('order/modify/<int:pk>', views.ModifyOrder.as_view(), name='order_modify'),
]