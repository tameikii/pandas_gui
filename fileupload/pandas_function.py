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
    graph_path = os.path.join(settings.MEDIA_ROOT, 'IMAGE/')
    graph_file_name = "pairplot_"+str(index)+".png"
    if not os.path.isdir(graph_path):
        os.makedirs(graph_path)
    sns.pairplot(df, palette="husl")
    plt.savefig(graph_path + graph_file_name)
    return graph_file_name
