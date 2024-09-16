# Degree Days Calculator

## Description
The **Degree Days Calculator** is a Python package designed to calculate Heating Degree Days (HDD) and Cooling Degree Days (CDD) based on temperature data. This tool is useful for energy consumption analysis, climate studies, and building energy efficiency calculations.

## Features
- Fetch temperature data from the Meteostat API
- Calculate mean temperatures
- Convert temperatures between Fahrenheit and Celsius
- Calculate Heating Degree Days (HDD) and Cooling Degree Days (CDD)
- Visualize degree days data

## Installation

To install the Degree Days Calculator, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/rmkenv/degree_days.git
2. Navigate to project directory:
   ```bash
   cd degree_days
3. Install
   ```bash
   pip install -e .

## Useage
```python
from degree_days.data_retrieval import fetch_temperature_data
from degree_days.degree_days import calculate_mean_temperature, calculate_degree_days, convert_base_temperature

# Fetch temperature data
start_date = '2022-01-01'
end_date = '2022-12-31'
latitude = 40.7128  # New York City
longitude = -74.0060

df = fetch_temperature_data(start_date, end_date, latitude, longitude)

# Calculate mean temperature
df = calculate_mean_temperature(df)

# Convert base temperature from Fahrenheit to Celsius
base_temp_f = 65
base_temp_c = convert_base_temperature(base_temp_f)

# Calculate Heating Degree Days (HDD)
hdd_df = calculate_degree_days(df, base_temp_c, degree_type='HDD')

# Calculate Cooling Degree Days (CDD)
cdd_df = calculate_degree_days(df, base_temp_c, degree_type='CDD')

# Print results
print(hdd_df)
print(cdd_df)
```


## API Reference

### data_retrieval.py

**`fetch_temperature_data(start_date, end_date, latitude, longitude)`**  
Fetches temperature data from the Meteostat API for a given location and time period.

### degree_days.py

**`convert_base_temperature(base_temp_f)`**  
Converts temperature from Fahrenheit to Celsius.

**`calculate_mean_temperature(df)`**  
Calculates the mean temperature from maximum and minimum temperatures.

**`calculate_degree_days(df, base_temp, degree_type='HDD')`**  
Calculates Heating Degree Days (HDD) or Cooling Degree Days (CDD) based on mean temperatures and a base temperature.

## Contributing

Contributions to the Degree Days Calculator are welcome! Please follow these steps to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Ryan Kmetz - [kmetzrm@gmail.com](mailto:kmetzrm@gmail.com)

Project Link: [https://github.com/rmkenv/degree_days](https://github.com/rmkenv/degree_days)
