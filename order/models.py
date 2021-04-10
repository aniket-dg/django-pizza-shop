from django.db import models
from multiselectfield import MultiSelectField

toppings_choices = (
        ('black_olives', 'Black Olives'),
        ('crisp_capsicum', 'Crisp Capsicum'),
        ('paneer', 'Paneer'),
        ('mushroom', 'Mushroom'),
        ('golden_corn', 'Golden Corn'),
        ('fresh_tomato', 'Fresh Tomato'),
        ('jalapeno', 'Jalapeno'),
        ('red_pepper', 'Red Pepper'),
        ('babycorn', 'Baby Corn'),
        ('italian_sausage', 'Italian Sausage'),
        ('italian_style_pork_topping','Italian Style Pork Topping'),
        ('pork_topping', 'Pork Topping'),
        ('beef_topping', 'Beef Topping'),
        ('sliced_pork_roll', 'Sliced Pork Roll'),
        ('quartered_ham', 'Quartered Ham'),
        ('bacon', 'Bacon'),
        
    )
pizza_type_choices = [
        ('Margherita', 'Margherita'),
        ('Double Cheese Margherita', 'Double Cheese Margherita'),
        ('Farm House', 'Farm House'),
        ('Peppy Paneer', 'Peppy Paneer'),
        ('Mexican Green Wave', 'Mexican Green Wave'),
        ('Deluxe Veggie', 'Deluxe Veggie'),
        ('Veg Extravaganza', 'Veg Extravaganza'),
        ('Cheese N Corn', 'Cheese N Corn'),
        ('Paneer Makhni', 'Paneer Makhni'),
        ('Veggi Paradise', 'Veggi Paradise'),
        ('Fresh Veggie', 'Fresh Veggie'),
        ('Indi Tandoori Paneer', 'Indi Tandoori Paneer'),
        ('Chicken Golden Delight', 'Chicken Golden Delight'),
        ('Non Veg Supreme', 'Non Veg Supreme'),
    ]
pizza_size_choices = [
        ('Small-8/20 cm', 'Small-8/20 cm'),
        ('Medium-10/25 cm', 'Medium-10/25 cm'),
        ('Large-12/30 cm', 'Large-12/30 cm'),
        ('X-Large-16/40 cm', 'X-Large-16/40 cm'),
        ('Italian-12/30 cm', 'Italian-12/30 cm'),
        ('Large-14/35 cm', 'Large-14/35 cm'),
        ('Family XXL-16/40cm', 'Family XXL-16/40cm'),
    ]

cheese_choices = [
        ('10 Ounces','10 Ounces'),
        ('8 Ounces','8 Ounces'),
        ('6 Ounces','6 Ounces'),
        ('3 Ounces','3 Ounces'),
        ('2 Ounces', '2 Ounces'),
    ]
class Order(models.Model):
    

    

    
    pizza_type = models.CharField(max_length=30, choices=pizza_type_choices, default='Margherita')
    pizza_size = models.CharField(max_length=30, choices=pizza_size_choices, default='Small-8"/20 cm')
    toppings = MultiSelectField(choices=toppings_choices, default=toppings_choices[0][0])
    cheese = models.CharField(max_length=30, choices=cheese_choices ,default='10 Ounces')
    no_of_pizza = models.IntegerField(primary_key=False, default=1)
    cust_name = models.CharField(max_length=30, blank=True, null= True)

    def __str__(self):
        return self.cust_name
