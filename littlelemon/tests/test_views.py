from django.test import TestCase
from restaurant.models import Menu
from django.core.serializers import serialize
import json

class MenuModelTest(TestCase):

    def setUp(self):
        # Add test instances of the Menu model here
        Menu.objects.create(title="Pancakes", price=5.99, inventory=20)
        Menu.objects.create(title="Burger", price=8.99, inventory=15)
        Menu.objects.create(title="Salad", price=7.50, inventory=30)

    def test_menu_creation(self):
        pancakes = Menu.objects.get(title="Pancakes")
        burger = Menu.objects.get(title="Burger")
        salad = Menu.objects.get(title="Salad")
        
        self.assertEqual(float(pancakes.price), 5.99)
        self.assertEqual(float(burger.price), 8.99)
        self.assertEqual(float(salad.price), 7.50)

        self.assertEqual(pancakes.inventory, 20)
        self.assertEqual(burger.inventory, 15)
        self.assertEqual(salad.inventory, 30)

    def test_getall(self):
        # Retrieve all Menu objects
        all_menus = Menu.objects.all()

        # Serialize the Menu objects
        serialized_menus = serialize('json', all_menus)
        serialized_data = json.loads(serialized_menus)

        # Expected serialized response
        expected_data = [
            {
                "model": "restaurant.menu",  
                "pk": 1,
                "fields": {
                    "title": "Pancakes",
                    "price": "5.99",
                    "inventory": 20
                }
            },
            {
                "model": "restaurant.menu",  
                "pk": 2,
                "fields": {
                    "title": "Burger",
                    "price": "8.99",
                    "inventory": 15
                }
            },
            {
                "model": "restaurant.menu",  
                "pk": 3,
                "fields": {
                    "title": "Salad",
                    "price": "7.50",
                    "inventory": 30
                }
            }
        ]

        # Assert that the serialized data matches the expected data
        for i, menu in enumerate(serialized_data):
            self.assertEqual(menu["fields"], expected_data[i]["fields"])
            self.assertEqual(menu["model"], expected_data[i]["model"])

