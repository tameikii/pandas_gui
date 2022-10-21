import os
import pandas
import datetime

from django.db import models
from django_pandas.io import read_frame
from django.core.validators import FileExtensionValidator
# Create your models here.

"""upload_toに渡すディレクトリ用の関数"""


def dir_path_name(instance, filename):
    date_time = datetime.datetime.now()
    date_dir = date_time.strftime('%Y/%m/%d')
    time_stamp = date_time.strftime('%H:%M/')
    new_filename = time_stamp + filename
    dir_path = os.path.join('CSV/', date_dir, new_filename)
    return dir_path


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class FileUploader(models.Model):
    """_summary_
    アップロード用のモデル
    """
    title = models.CharField(default="CSVファイル", max_length=50)
    upload_dir = models.FileField(upload_to=dir_path_name,
                                  validators=[FileExtensionValidator(['csv', ])],
                                  )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def file_name(self):
        """
        相対パスからファイル名のみを取得するカスタムメソッド
        """
        path = os.path.basename(self.upload_dir.name)
        return path


class FileList(models.Model):

    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
