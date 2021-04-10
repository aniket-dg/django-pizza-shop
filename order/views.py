from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Order
import json
from django.contrib import messages
from .forms import OrderForm
# Create your views here.

def orderGenerate(request):
    if request.method == "POST":
        orderData = OrderForm(request.POST)
        if orderData.is_valid():
            order = orderData.save()
            messages.success(request, "Order Placed Successfully. Your order id is {id}".format(id = order.id))
            return redirect('/shop')
    else:
        form1 = OrderForm(initial={ 'toppings':'Black Olives' })
        return render(request, 'index.html', { 'form1': form1 })