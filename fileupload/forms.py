from django import forms
from .models import FileUploader


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUploader
        fields = ('title', 'upload_dir',)
