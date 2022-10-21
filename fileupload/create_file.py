from django.conf import settings
from .models import FileList, FileUploader
import os
from django_pandas.io import read_frame
# ファイルを書き込む際に渡す絶対パス
media_path = os.path.join(settings.MEDIA_ROOT,)


# mediarootとFileUploaderに渡す相対ぱす
path = os.path.join('auto_upload_file', '')

# ファイルを更新する関数


def pandas_csv(df, path):
