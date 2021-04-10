# Generated by Django 3.2 on 2021-04-09 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Toppings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('black_olives', models.BooleanField(default=True)),
                ('crisp_capsicum', models.BooleanField(default=False)),
                ('paneer', models.BooleanField(default=False)),
                ('mushroom', models.BooleanField(default=False)),
                ('golden_corn', models.BooleanField(default=False)),
                ('fresh_tomato', models.BooleanField(default=False)),
                ('jalapeno', models.BooleanField(default=False)),
                ('red_pepper', models.BooleanField(default=False)),
                ('babycorn', models.BooleanField(default=False)),
                ('italian_sausage', models.BooleanField(default=False)),
                ('italian_style_pork_topping', models.BooleanField(default=False)),
                ('pork_topping', models.BooleanField(default=False)),
                ('beef_topping', models.BooleanField(default=False)),
                ('sliced_pork_roll', models.BooleanField(default=False)),
                ('quartered_ham', models.BooleanField(default=False)),
                ('bacon', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_type', models.CharField(choices=[('Margherita', '0'), ('Double Cheese Margherita', '1'), ('Farm House', '2'), ('Peppy Paneer', '3'), ('Mexican Green Wave', '4'), ('Deluxe Veggie', '5'), ('Veg Extravaganza', '6'), ('Cheese N Corn', '7'), ('Paneer Makhni', '8'), ('Veggi Paradise', '9'), ('Fresh Veggie', '10'), ('Indi Tandoori Paneer', '11'), ('Chicken Golden Delight', '12'), ('Non Veg Supreme', '13')], default='Margherita', max_length=30)),
                ('pizza_size', models.CharField(choices=[('Small-8"/20 cm', '0'), ('Medium-10"/25 cm', '1'), ('Large-12"/30 cm', '2'), ('X-Large-16"/40 cm', '3'), ('Italian-12"/30 cm', '4'), ('Large-14"/35 cm', '5'), ('Family XXL-16"/40cm', '6')], default='Small-8"/20 cm', max_length=30)),
                ('cheese', models.CharField(default='10 Ounces', max_length=30)),
                ('no_of_pizza', models.IntegerField()),
                ('cust_name', models.CharField(max_length=30)),
                ('toppings', models.ManyToManyField(to='order.Toppings')),
            ],
        ),
    ]
