from django import forms
from .models import FileUploader


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUploader
        fields = {'description', 'upload_file'}
