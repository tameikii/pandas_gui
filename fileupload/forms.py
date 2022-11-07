from email.policy import default
from django import forms
from .models import FileUploader


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUploader
        fields = ('upload_dir',)


# 新規ファイル作成時のファイルの名前を受け取る
class FilenameForm(forms.Form):
    file_name = forms.CharField(max_length=100)
