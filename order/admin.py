from django.contrib import admin
from .models import Order
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','cust_name', 'pizza_type', 'pizza_size' , 'no_of_pizza')

admin.site.register(Order, OrderAdmin)