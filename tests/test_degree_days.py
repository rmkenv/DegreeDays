import os
import pandas as pd
from degree_days.data_retrieval import fetch_temperature_data
from degree_days.degree_days import convert_base_temperature, calculate_mean_temperature, calculate_degree_days

# Set the API key for Meteostat
os.environ['METEOSTAT_API_KEY'] = 'your_api_key_here'

def test_convert_base_temperature():
  base_temp_f = 65
  base_temp_c = convert_base_temperature(base_temp_f)
  assert round(base_temp_c, 2) == 18.33, f"Expected 18.33 but got {base_temp_c}"

def test_calculate_mean_temperature():
  data = {'tmax': [30, 25, 20], 'tmin': [10, 5, 0]}
  df = pd.DataFrame(data)
  
  df = calculate_mean_temperature(df)
  
  assert df['TMEAN'][0] == 20, f"Expected 20 but got {df['TMEAN'][0]}"
  assert df['TMEAN'][1] == 15, f"Expected 15 but got {df['TMEAN'][1]}"
  assert df['TMEAN'][2] == 10, f"Expected 10 but got {df['TMEAN'][2]}"

def test_calculate_degree_days_hdd():
  data = {'TMEAN': [20, 15, 10, 25]}
  df = pd.DataFrame(data)
  
  base_temp_c = 18.33  # Converted 65°F to Celsius
  
  df = calculate_degree_days(df, base_temp_c, degree_type='HDD')
  
  assert df['DegreeDays'][0] == 0, f"Expected 0 but got {df['DegreeDays'][0]}"
  assert round(df['DegreeDays'][1], 2) == 3.33, f"Expected 3.33 but got {df['DegreeDays'][1]}"
  assert round(df['DegreeDays'][2], 2) == 8.33, f"Expected 8.33 but got {df['DegreeDays'][2]}"
  assert df['DegreeDays'][3] == 0, f"Expected 0 but got {df['DegreeDays'][3]}"

def test_calculate_degree_days_cdd():
  data = {'TMEAN': [20, 25, 30, 10]}
  df = pd.DataFrame(data)
  
  base_temp_c = 18.33  # Converted 65°F to Celsius
  
  df = calculate_degree_days(df, base_temp_c, degree_type='CDD')
  
  assert round(df['DegreeDays'][0], 2) == 1.67, f"Expected 1.67 but got {df['DegreeDays'][0]}"
  assert round(df['DegreeDays'][1], 2) == 6.67, f"Expected 6.67 but got {df['DegreeDays'][1]}"
  assert round(df['DegreeDays'][2], 2) == 11.67, f"Expected 11.67 but got {df['DegreeDays'][2]}"
  assert df['DegreeDays'][3] == 0, f"Expected 0 but got {df['DegreeDays'][3]}"

def test_fetch_temperature_data():
  start_date = '2022-01-01'
  end_date = '2022-01-05'
  latitude = 52.52
  longitude = 13.405
  
  df = fetch_temperature_data(start_date, end_date, latitude, longitude)
  
  assert 'tmin' in df.columns, "tmin column is missing"
  assert 'tmax' in df.columns, "tmax column is missing"
  assert len(df) > 0, "No data was fetched from Meteostat"

if __name__ == '__main__':
  import unittest
  unittest.main()
