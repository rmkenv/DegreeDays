# data_retrieval.py
import os
import pandas as pd
from meteostat import Daily, Point

def fetch_temperature_data(start_date, end_date, latitude, longitude):
  """
  Fetch daily temperature data from Meteostat for a given location and time period.
  
  Parameters:
  - start_date: str or datetime, start of the period
  - end_date: str or datetime, end of the period
  - latitude: float, latitude of the location
  - longitude: float, longitude of the location
  
  Returns:
  - pandas DataFrame with temperature data
  """
  
  api_key = os.getenv('METEOSTAT_API_KEY')
  
  if not api_key:
      raise ValueError("You must set your Meteostat API key as an environment variable 'METEOSTAT_API_KEY'.")

  # Meteostat now uses the API key automatically if it's set as an environment variable
  # So we don't need to explicitly set it

  location = Point(latitude, longitude)
  data = Daily(location, start_date, end_date)
  data = data.fetch()

  # Return relevant temperature columns (tavg, tmin, tmax)
  return data[['tavg', 'tmin', 'tmax']]
