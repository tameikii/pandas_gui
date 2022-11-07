import pandas as pd
import pandas_profiling as pdp
import matplotlib


def show_data_profiling(df):
    profile = pdp.ProfileReport(df)
    return profile.to_file("profile.html")


def get_df_type(df):
    df_type_list = list()
    df = pd.DataFrame(df)
    columns = df.columns
    for col in columns:
        col_type = df[col].dtypes
        col_type = str(col_type).split("'")
        df_type_list.append(col_type[0])
    return df_type_list
