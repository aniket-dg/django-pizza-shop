from django import forms
from order.models import toppings_choices, pizza_type_choices, pizza_size_choices, cheese_choices

class OrderForm(forms.Form):
    pizza_type = forms.ChoiceField(choices=pizza_type_choices)
    pizza_size = forms.ChoiceField(choices= pizza_size_choices)
    toppings = forms.MultipleChoiceField( widget=forms.CheckboxSelectMultiple,choices=toppings_choices, required=True)
    cheese = forms.ChoiceField(choices=cheese_choices)
    no_of_pizza = forms.IntegerField()
    cust_name = forms.CharField(max_length=30)
