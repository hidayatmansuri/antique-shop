from django import forms
from .models import Antq

class AntqForm(forms.ModelForm):
    class Meta:
        model = Antq
        fields = ('name', 'price', 'manufacture', 'description', 'height', 'width', 'depth')