from django.test import TestCase
from . import Menu

class MenuModelTestCase(TestCase):
    def setUp(self):
        Menu.objects.create(title='IceCream', price=10.99, inventory=100)

    def test_menu_str_method(self):
        iceCream = Menu.objects.get(title='IceCream')
        self.assertEqual(str(iceCream), 'Burger : 10.99')

    def test_menu_inventory(self):
        iceCream = Menu.objects.get(title='IceCream')
        self.assertEqual(iceCream.inventory, 100)