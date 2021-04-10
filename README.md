# django-pizza-shop
Sample Project to create api for Pizza Order CRUD Operations


## Installation

```
https://github.com/aniket-dg/django-pizza-shop.git
```

Create VirtualEnv and Activate it

Go to the Project Folder
```
cd django-pizza-shop
```
Install all required Libraries
```
pip install -r requirements.txt
```

## Database Configuration
1. Create database pizza-shop
1. Open pizza_shop/settings.py
     1. In the databse configuraton change USER & PASSWORD field to yours.

Apply Migrations
```
python manage.py migrate
```
Start the Project
```
python manage.py runserver
```
Go to the 127.0.0.1:8000/

## Documentation

API methods and their Endpoints

|  Method |    Endpoint     |   Description  |
|---------|-----------------|----------------|
| GET     |    /api/        | Get the List of all Orders |
| DELETE     |    /api/        | Delete all orders |
| POST     |    /api/order/create        | Create new Order |
| GET     |    /api/order/modify/\<id\>        | Returns a Specific Order |
| PUT     |    /api/order/modify/\<id\>        | Update the existing Order with given id |
| DELETE     |    /api/order/modify/\<id\>        | Delete the order with specific id |

