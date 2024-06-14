from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework.test import APIClient
from rest_framework import status

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

        self.menu_item1 = Menu.objects.create(title='Pizza', price=10.99, inventory=100)
        self.menu_item2 = Menu.objects.create(title='Burger', price=8.99, inventory=100)
        self.menu_item3 = Menu.objects.create(title='Salad', price=5.99, inventory=20)

    def test_get_all_menu_items(self):
        response = self.client.get(reverse('menu-items'))  # Adjust 'menuitem-list' to match your URL name
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)