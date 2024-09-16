%%writefile /content/degree_days/tests/test_degree_days.py
import os
import unittest
import pandas as pd
from datetime import datetime
from degree_days.data_retrieval import fetch_temperature_data
from degree_days.degree_days import convert_base_temperature, calculate_mean_temperature, calculate_degree_days

class TestDegreeDays(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set the API key for Meteostat
        os.environ['METEOSTAT_API_KEY'] = 'your_api_key_here'

    def test_convert_base_temperature(self):
        base_temp_f = 65
        base_temp_c = convert_base_temperature(base_temp_f)
        self.assertAlmostEqual(base_temp_c, 18.33, places=2)

    def test_calculate_mean_temperature(self):
        data = {'tmax': [30, 25, 20], 'tmin': [10, 5, 0]}
        df = pd.DataFrame(data)
        
        df = calculate_mean_temperature(df)
        
        self.assertEqual(df['TMEAN'][0], 20)
        self.assertEqual(df['TMEAN'][1], 15)
        self.assertEqual(df['TMEAN'][2], 10)

    def test_calculate_degree_days_hdd(self):
        data = {'TMEAN': [20, 15, 10, 25]}
        df = pd.DataFrame(data)
        
        base_temp_c = 18.33  # Converted 65°F to Celsius
        
        df = calculate_degree_days(df, base_temp_c, degree_type='HDD')
        
        self.assertAlmostEqual(df['DegreeDays'][0], 0, places=2)
        self.assertAlmostEqual(df['DegreeDays'][1], 3.33, places=2)
        self.assertAlmostEqual(df['DegreeDays'][2], 8.33, places=2)
        self.assertEqual(df['DegreeDays'][3], 0)

    def test_calculate_degree_days_cdd(self):
        data = {'TMEAN': [20, 25, 30, 10]}
        df = pd.DataFrame(data)
        
        base_temp_c = 18.33  # Converted 65°F to Celsius
        
        df = calculate_degree_days(df, base_temp_c, degree_type='CDD')
        
        self.assertAlmostEqual(df['DegreeDays'][0], 1.67, places=2)
        self.assertAlmostEqual(df['DegreeDays'][1], 6.67, places=2)
        self.assertAlmostEqual(df['DegreeDays'][2], 11.67, places=2)
        self.assertEqual(df['DegreeDays'][3], 0)

    def test_fetch_temperature_data(self):
        start_date = datetime(2022, 1, 1)
        end_date = datetime(2022, 1, 5)
        latitude = 52.52
        longitude = 13.405
        
        df = fetch_temperature_data(start_date, end_date, latitude, longitude)
        
        self.assertIn('tmin', df.columns)
        self.assertIn('tmax', df.columns)
        self.assertIn('tavg', df.columns)
        self.assertGreater(len(df), 0)

if __name__ == '__main__':
    unittest.main()
