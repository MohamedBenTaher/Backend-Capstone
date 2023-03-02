from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuItemsViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        self.client.force_authenticate(user=self.user)

        self.menu_item1 = Menu.objects.create(
            title='Item 1', price=10.99, inventory=50
        )
        self.menu_item2 = Menu.objects.create(
            title='Item 2', price=5.99, inventory=25
        )

        self.url = reverse('menu')

    def test_get_menu_items(self):
        response = self.client.get(self.url)

        expected_data = MenuSerializer([self.menu_item1, self.menu_item2], many=True).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_create_menu_item(self):
        data = {
            'title': 'Item 3',
            'price': 15.99,
            'inventory': 75
        }

        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 3)
        self.assertEqual(Menu.objects.last().title, data['title'])
