# Generated by Django 3.2 on 2021-04-10 04:06

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20210410_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='toppings',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('black_olives', 'Black Olives'), ('crisp_capsicum', 'Crisp Capsicum'), ('paneer', 'Paneer'), ('mushroom', 'Mushroom'), ('golden_corn', 'Golden Corn'), ('fresh_tomato', 'Fresh Tomato'), ('jalapeno', 'Jalapeno'), ('red_pepper', 'Red Pepper'), ('babycorn', 'Baby Corn'), ('italian_sausage', 'Italian Sausage'), ('italian_style_pork_topping', 'Italian Style Pork Topping'), ('pork_topping', 'Pork Topping'), ('beef_topping', 'Beef Topping'), ('sliced_pork_roll', 'Sliced Pork Roll'), ('quartered_ham', 'Quartered Ham'), ('bacon', 'Bacon')], default='black_olives', max_length=203),
        ),
    ]
