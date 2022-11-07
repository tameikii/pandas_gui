from distutils.command.upload import upload
from django.conf import settings
from .models import FileList, FileUploader
from django.shortcuts import get_object_or_404, render, redirect
import os
import datetime
import pandas as pd
from django_pandas.io import read_frame


# ファイルを更新する関数
def pandas_csv(df, filename):
    update_path = os.path.join(settings.MEDIA_ROOT, 'CSV/', filename)
    df.to_csv(update_path)
    FileUploader.objects.update_or_create(upload_dir=update_path)
    tmp = FileUploader.objects.get(upload_dir=update_path)
    return tmp.id

# 新規ファイルの作成する関数


def create_csv(df, newfilename):
    media_path = os.path.join(settings.MEDIA_ROOT, 'CSV/', newfilename)
    df.to_csv(media_path)
    tmp = FileUploader(upload_dir=media_path)
    tmp.save()
    return tmp.id
