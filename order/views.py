from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Order
import json
from django.contrib import messages
from .forms import OrderForm
# Create your views here.

def orderGenerate(request):
    if request.method == "POST":
        pizza_type = request.POST['pizza_type']
        pizza_size = request.POST['pizza_size']
        order = Order(pizza_type = request.POST['pizza_type'],
                      pizza_size = request.POST['pizza_size'],
                      cheese = request.POST['cheese'],
                      no_of_pizza = request.POST['no_of_pizza'],
                      cust_name = request.POST['cust_name']  
        )
        toppings = [ 'Black Olives', 'Crisp Capsicum','Paneer', 'Mushroom',
                'Golden Corn', 'Fresh Tomato', 'Jalapeno','Red Pepper',
                'Babycorn','Italian Sausage', 'Italian Style Pork Topping',
                'Pork Topping', 'Beef Topping', 'Sliced Pork Roll',
                'Quartered Ham', 'Bacon' ]
        topping_index = request.POST.getlist('toppings[]')
        topping_list = []
        for index in topping_index:
            topping_list.append(toppings[int(index)])
        toppings = json.dumps(topping_list)
        order.toppings = toppings
        order.save()
        messages.success(request, "Order Placed Successfully. Your order id is : {id}".format(id = order.id))
        return redirect('/shop')
    else:
        form1 = OrderForm(initial={ 'toppings':'Black Olives' })
        return render(request, 'index.html', { 'form1': form1 })