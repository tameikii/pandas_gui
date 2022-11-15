import base64
from django.conf import settings
import datetime
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import io
import os
import pandas as pd
import pandas_profiling as pdp
import matplotlib
matplotlib.use('agg')


def create_data_profiling(df):
    profile = pdp.ProfileReport(df)
    output_file = "fileupload/templates/fileupload/profile.html"
    profile.to_file(output_file)


def get_df_type(df):
    df_type_list = list()
    df = pd.DataFrame(df)
    columns = df.columns
    for col in columns:
        col_type = df[col].dtypes
        col_type = str(col_type).split("'")
        df_type_list.append(col_type[0])
    return df_type_list


def create_df_info(df):
    buffer = io.StringIO()
    df.info(buf=buffer)
    df_info = buffer.getvalue().split("\n")
    return df_info


def create_df_describe(df):
    return df.describe(include="all")


def create_sns_pairplot(df, index):
    graph_path = os.path.join(settings.MEDIA_ROOT, 'images/', 'pair/')
    graph_file_name = "pairplot_"+str(index)+".png"
    if not os.path.isdir(graph_path):
        os.makedirs(graph_path)
    plt.clf()
    sns.pairplot(df)
    plt.savefig(graph_path + graph_file_name)
    return graph_file_name


def create_sns_boxplot(df, index):
    graph_path = os.path.join(settings.MEDIA_ROOT, 'images/', 'box/')
    graph_file_name = "boxplot_"+str(index)+".png"
    if not os.path.isdir(graph_path):
        os.makedirs(graph_path)
    plt.clf()
    sns.boxplot(data=df)
    plt.savefig(graph_path + graph_file_name)
    return graph_file_name


def create_sns_heatmap(df, index):
    graph_path = os.path.join(settings.MEDIA_ROOT, 'images/', 'heatmap/')
    graph_file_name = "heatmap_"+str(index)+".png"
    if not os.path.isdir(graph_path):
        os.makedirs(graph_path)
    plt.clf()
    plt.figure(figsize=(10, 10))
    options = {'square': True, 'annot': True, 'fmt': '0.2f', 'xticklabels': df.columns,
               'yticklabels': df.columns, 'annot_kws': {'size': 12}, 'vmin': -1, 'vmax': 1, 'center': 0, 'cbar': False}
    ax = sns.heatmap(df.corr(), **options)
    ax.tick_params(axis='x', labelsize=10)
    ax.tick_params(axis='y', labelsize=10)
    plt.savefig(graph_path + graph_file_name)
    return graph_file_name
