
from turtle import title
from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_Menu(self):
        item=Menu.objects.create(ID=4,Title="iceCream",Price=80,Inventory=100)
        self.assertEqual(str(item),"iceCream: 80")