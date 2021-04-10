from django import forms
from order.models import toppings_choices, pizza_type_choices, pizza_size_choices, cheese_choices, Order

class OrderForm(forms.Form):
    pizza_type = forms.ChoiceField(choices=pizza_type_choices)
    pizza_size = forms.ChoiceField(choices= pizza_size_choices)
    toppings = forms.MultipleChoiceField( widget=forms.CheckboxSelectMultiple,choices=toppings_choices, required=True)
    cheese = forms.ChoiceField(choices=cheese_choices)
    no_of_pizza = forms.IntegerField()
    cust_name = forms.CharField(max_length=30)
    def save(self):
        order = Order.objects.create(
            pizza_type = self.cleaned_data['pizza_type'],
            pizza_size = self.cleaned_data['pizza_size'],
            toppings = self.cleaned_data['toppings'],
            cheese = self.cleaned_data['cheese'],
            no_of_pizza = self.cleaned_data['no_of_pizza'],
            cust_name = self.cleaned_data['cust_name']
        )
        return order
