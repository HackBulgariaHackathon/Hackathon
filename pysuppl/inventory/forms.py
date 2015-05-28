from django.forms import ModelForm
from .models import Computer

class ComputerForm(ModelForm):
    class Meta:
        model = Computer
        fields = ['vendor_id', 'serial', 'date_bought', 'name']


