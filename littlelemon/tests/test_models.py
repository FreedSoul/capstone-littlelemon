from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_an_item(self):
        item = Menu.objects.create(title='spaghetti',price=5.77,inventory=2)
        self.assertEqual(str(item), "spaghetti : 5.77")