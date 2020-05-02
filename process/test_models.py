from django.test import TestCase
from .models import Antq

class TestAntqModel(TestCase):
    def test_can_create_an_antique_with_name_and_price(self):
        antq = Antq(name="Create a Test", price="395")
        antq.save()
        self.assertEqual(antq.name, "Create a Test")
        self.assertEqual(antq.price, "395")
        
    def test_item_as_string(self):
        antq = Antq(name="Create a Test")
        self.assertEqual("Create a Test", str(antq))