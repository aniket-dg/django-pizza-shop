from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListOrder.as_view(), name='order_list'), # Api index page - View All Orders
    path('order/create', views.CreateOrder.as_view(), name='order_create'), # API new Order
    path('order/modify/<int:pk>', views.ModifyOrder.as_view(), name='order_modify'), # MOdify Order
]