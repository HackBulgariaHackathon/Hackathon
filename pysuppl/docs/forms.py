from django.forms import ModelForm
from .models import Document


class DocumentForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.uploader = kwargs.pop('user')
        super(DocumentForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Document
        fields = ['name', 'serial', 'tags', 'file']

    def save(self, *args, **kwargs):
        self.instance.uploader = self.uploader
        return super(DocumentForm, self).save()
