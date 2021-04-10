import pandas as pd

def read_list(filepath):
    return pd.read_csv(filepath)

def remove_columns(df):
    return df.drop(['user_id', 'user_name', 'user_total_anime', 
    'user_total_watching', 'user_total_completed', 'user_total_onhold', 
    'user_total_dropped', 'user_total_plantowatch', 'user_export_type',
    'my_id', 'my_start_date', 'my_finish_date', 'my_rated', 'my_score',
    'my_storage', 'my_storage_value', 'my_comments', 'my_times_watched',
    'my_rewatch_value', 'my_priority', 'my_tags', 'my_rewatching', 
    'my_rewatching_ep', 'my_discuss', 'my_sns', 'update_on_import'], axis=1)