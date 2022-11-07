import datetime
import os
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView
from fileupload.pandas_function import show_data_profiling
from .forms import FileUploadForm, FilenameForm
from .models import FileUploader, FileList, dir_path_name
from .create_file import pandas_csv, create_csv
from .pandas_function import show_data_profiling, get_df_type
from django_pandas.io import pd as dpd
import pandas as pd
import pandas_profiling as pdp
from django.conf import settings

# Create your views here.


def index(request):
    """
    トップページ
    DBに保存されているCSVファイルのリストを表示
    """
    file_obj = FileUploader.objects.all()
    # 保存データからのアップロード要としてフィルターをかけて取得
    return render(request, 'fileupload/index.html', {'file_obj': file_obj})


"""------------------アップロードページ-----------------------"""


def new_file(request):
    """ファイルアップロード"""
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fileupload:index')
    else:
        form = FileUploadForm()
    return render(request, 'fileupload/new_file.html', {'form': form})


def detail(request, pk):
    """詳細ページ"""
    file_value = get_object_or_404(FileUploader, id=pk)
    try:
        # utf-8に対応
        df = pd.read_csv(file_value.upload_dir.path, index_col=0)

    except UnicodeDecodeError:
        df = pd.read_csv(file_value.upload_dir.path, index_col=0)
    df_type_list = get_df_type(df)
    context = {
        'file_value': file_value,
        'df': df,
        'df_type_list': df_type_list,
    }
    return render(request, 'fileupload/detail.html', context)


def delete(request, pk):
    file_value = get_object_or_404(FileUploader, id=pk)
    ctx = {"file_value": file_value}
    if request.POST:
        file_value.delete()
        return redirect('fileupload:index')
    return render(request, 'fileupload/delete.html', ctx)
