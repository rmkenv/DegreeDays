import pandas as pd

def convert_base_temperature(base_temp_f):
    return (base_temp_f - 32) * 5/9

def calculate_mean_temperature(df):
    if 'tavg' in df.columns:
        df['TMEAN'] = df['tavg']
    elif 'tmax' in df.columns and 'tmin' in df.columns:
        df['TMEAN'] = (df['tmax'] + df['tmin']) / 2
    else:
        raise ValueError("DataFrame must contain either 'tavg' column or both 'tmax' and 'tmin' columns")
    return df

def calculate_degree_days(df, base_temp, degree_type='HDD'):
    if degree_type == 'HDD':
        df['DegreeDays'] = df['TMEAN'].apply(lambda x: max(0, base_temp - x))
    elif degree_type == 'CDD':
        df['DegreeDays'] = df['TMEAN'].apply(lambda x: max(0, x - base_temp))
    else:
        raise ValueError("degree_type must be either 'HDD' or 'CDD'")
    return df
