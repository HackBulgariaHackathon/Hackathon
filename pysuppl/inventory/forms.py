from django.forms import ModelForm
from .models import Computer, Software

class ComputerForm(ModelForm):
    class Meta:
        model = Computer
        fields = ['vendor_id', 'serial',
                  'date_bought', 'name', 'owner']


class SoftwareForm(ModelForm):
    class Meta:
        model = Software
        fields = ['name', 'description', 'vendor_id', 'license_id']
