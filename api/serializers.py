from rest_framework import serializers, fields
from order.models import Order, toppings_choices

class OrderSerializer(serializers.ModelSerializer):
    toppings = fields.MultipleChoiceField(choices=toppings_choices)
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Order
        fields = [ 'id','pizza_type', 'pizza_size', 'toppings','cheese', 'no_of_pizza', 'cust_name' ]
    