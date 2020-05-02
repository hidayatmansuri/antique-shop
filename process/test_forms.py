from django.test import TestCase
from .forms import AntqForm

# Create your tests here.
class TestAntqForm(TestCase):
    
    def test_can_not_create_without_name(self):
        form =AntqForm({'name': 'Create test'})
        self.assertFalse(form.is_valid())
        
    def test_correct_messgae_for_missing_name(self):
        form =AntqForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])