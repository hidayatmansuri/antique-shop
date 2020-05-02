from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Antq

class TestViews(TestCase):
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
        
    def test_get_add_item_page(self):
        page = self.client.get("/add")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "addantique.html")
        
    def test_get_edit_item_page(self):
        antq = Antq(name='Create a test')
        antq.save()
        
        page = self.client.get("/edit/{0}".format(antq.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "addantique.html")
        
    def test_get_edit_page_for_item_that_does_not_exist(self):
        page = self.client.get("/edit/1")
        self.assertEqual(page.status_code, 404)
        
    def test_post_add_antique(self):
        response = self.client.post("/add", {"name": "Add Antique"})
        antq = get_object_or_404(Antq, pk=1)
        self.assertEqual(antq.name, False)
        
    def test_post_edit_antique(self):
        antq = Antq(name="Add Antique")
        antq.save()
        id = antq.id
        
        response = self.client.post("/edit/{0}".format(id), {"name": "A different name"})
        antq = get_object_or_404(Antq, pk=id)
        self.assertEqual("Add Antique", antq.name)