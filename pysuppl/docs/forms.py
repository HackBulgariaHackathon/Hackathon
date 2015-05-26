from django.forms import ModelForm
from .models import Document

class DocumentForm(ModelForm):
    class meta:
        model = Document
        fields = ['serial', 'name', 'uploader', 'department', 'uploaded', 'doc',
                  'uploaded']
