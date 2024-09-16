# degree_days.py

def convert_base_temperature(base_temp_f):
    """
    Convert the base temperature from Fahrenheit to Celsius.
    """
    return (base_temp_f - 32) * 5.0 / 9.0

def calculate_mean_temperature(df):
    """
    Calculate the mean temperature (TMEAN) from daily minimum and maximum temperatures.
    """
    df['TMEAN'] = (df['tmax'] + df['tmin']) / 2
    df['TMEAN'].fillna(df['tavg'], inplace=True)  # Use tavg if available
    df.dropna(subset=['TMEAN'], inplace=True)
    return df

def calculate_degree_days(df, base_temp_c, degree_type='HDD'):
    """
    Calculate Heating Degree Days (HDD) or Cooling Degree Days (CDD).
    
    Parameters:
    - df: pandas DataFrame containing the temperature data
    - base_temp_c: base temperature in Celsius
    - degree_type: 'HDD' for heating degree days or 'CDD' for cooling degree days
    
    Returns:
    - DataFrame with DegreeDays calculated
    """
    if degree_type == 'HDD':
        df['DegreeDays'] = base_temp_c - df['TMEAN']
    elif degree_type == 'CDD':
        df['DegreeDays'] = df['TMEAN'] - base_temp_c
    else:
        raise ValueError("degree_type must be 'HDD' or 'CDD'")
    
    df['DegreeDays'] = df['DegreeDays'].apply(lambda x: max(x, 0))  # HDD or CDD cannot be negative
    return df
