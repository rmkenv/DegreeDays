# data_retrieval.py
import os
from typing import Union
from datetime import datetime

import pandas as pd
from meteostat import Daily, Point
from meteostat.core import set_api_key

def fetch_temperature_data(
  start_date: Union[str, datetime],
  end_date: Union[str, datetime],
  latitude: float,
  longitude: float
) -> pd.DataFrame:
  """
  Fetch daily temperature data from Meteostat for a given location and time period. Requires Meteostat API Key.
  
  Parameters:
  - start_date: str or datetime, start of the period
  - end_date: str or datetime, end of the period
  - latitude: float, latitude of the location
  - longitude: float, longitude of the location
  
  Returns:
  - pandas DataFrame with temperature data columns:
    - tavg: average temperature
    - tmin: minimum temperature
    - tmax: maximum temperature
  
  Raises:
  - ValueError: If the Meteostat API key is not set
  - Exception: If there's an error fetching data from Meteostat
  """

  api_key = os.getenv('METEOSTAT_API_KEY')
  
  if not api_key:
      raise ValueError("You must set your Meteostat API key as an environment variable 'METEOSTAT_API_KEY'.")

  # Set the API key for Meteostat
  set_api_key(api_key)

  location = Point(latitude, longitude)
  
  try:
      data = Daily(location, start_date, end_date)
      data = data.fetch()
  except Exception as e:
      raise Exception(f"Error fetching data from Meteostat: {str(e)}")

  # Return relevant temperature columns (tavg, tmin, tmax)
  return data[['tavg', 'tmin', 'tmax']]

# Created/Modified files during execution:
print("data_retrieval.py")
