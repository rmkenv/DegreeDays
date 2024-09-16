# Degree Days Calculator

## Description
The Degree Days Calculator is a Python package designed to calculate Heating Degree Days (HDD) and Cooling Degree Days (CDD) based on temperature data. This tool is useful for energy consumption analysis, climate studies, and building energy efficiency calculations.

## Features
- Fetch temperature data from Meteostat API
- Calculate mean temperatures
- Convert temperatures between Fahrenheit and Celsius
- Calculate Heating Degree Days (HDD) and Cooling Degree Days (CDD)
- Visualize degree days data

## Installation

To install the Degree Days Calculator, follow these steps:

1. Clone the repository:
git clone https://github.com/rmkenv/degree_days.git


2. Navigate to the project directory:
cd degree_days


3. Install the package and its dependencies:
pip install -e .


## Usage

Here's a basic example of how to use the Degree Days Calculator:

python
from degree_days.data_retrieval import fetch_temperature_data
from degree_days.degree_days import calculate_mean_temperature, calculate_degree_days, convert_base_temperature

Fetch temperature data
start_date = '2022-01-01'
end_date = '2022-12-31'
latitude = 40.7128  # New York City
longitude = -74.0060

df = fetch_temperature_data(start_date, end_date, latitude, longitude)

Calculate mean temperature
df = calculate_mean_temperature(df)

Convert base temperature from Fahrenheit to Celsius
base_temp_f = 65
base_temp_c = convert_base_temperature(base_temp_f)

Calculate Heating Degree Days
hdd_df = calculate_degree_days(df, base_temp_c, degree_type='HDD')

Calculate Cooling Degree Days
cdd_df = calculate_degree_days(df, base_temp_c, degree_type='CDD')

Print results
print(hdd_df)
print(cdd_df)


## API Reference

### `data_retrieval.py`

#### `fetch_temperature_data(start_date, end_date, latitude, longitude)`
Fetches temperature data from the Meteostat API for a given location and time period.

### `degree_days.py`

#### `convert_base_temperature(base_temp_f)`
Converts temperature from Fahrenheit to Celsius.

#### `calculate_mean_temperature(df)`
Calculates the mean temperature from maximum and minimum temperatures.

#### `calculate_degree_days(df, base_temp, degree_type='HDD')`
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

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Your Name - [your-email@example.com](mailto:your-email@example.com)

Project Link: [https://github.com/rmkenv/degree_days](https://github.com/rmkenv/degree_days)
This README provides a comprehensive overview of your project, including:

A brief description
Key features
Installation instructions
Usage example
API reference
Contributing guidelines
License information
Contact information
You may want to adjust some parts, such as the contact information and any specific details about the project that I might have missed or interpreted incorrectly. Also, consider adding more detailed usage examples, information about any configuration needed (like API keys), and any known limitations or future plans for the project.

Would you like me to modify or expand on any part of this README?Based on the repository content, here's a comprehensive README for the degree_days project:

degree_days
A Python library for calculating Heating Degree Days (HDD) and Cooling Degree Days (CDD) using weather data from Meteostat and applying linear regression for energy use modeling.

Features
Fetch temperature data from Meteostat API
Calculate Heating Degree Days (HDD) and Cooling Degree Days (CDD)
Perform linear regression for energy use modeling
Easy-to-use interface for environmental monitoring and analysis
Installation
Install the library using pip:

pip install degree_days
Requirements
Python 3.6+
pandas>=1.1
numpy>=1.19
scikit-learn>=0.24
matplotlib>=3.3
meteostat>=1.5
Usage
Here's a basic example of how to use the degree_days library:

python
Execute
Copy Code
from degree_days import fetch_temperature_data, calculate_degree_days
from datetime import datetime

# Fetch temperature data
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 12, 31)
latitude = 40.7128
longitude = -74.0060

df = fetch_temperature_data(start_date, end_date, latitude, longitude)

# Calculate Heating Degree Days
base_temp = 18  # Celsius
hdd = calculate_degree_days(df, base_temp, degree_type='HDD')

# Calculate Cooling Degree Days
cdd = calculate_degree_days(df, base_temp, degree_type='CDD')

print(f"Total HDD: {hdd['DegreeDays'].sum()}")
print(f"Total CDD: {cdd['DegreeDays'].sum()}")
API Key
To use this library, you need to sign up for a Meteostat API key:
https://dev.meteostat.net/api/#sign-up

Once you have your API key, set it as an environment variable:

export METEOSTAT_API_KEY='your_api_key_here'
Documentation
For detailed documentation, please refer to the docstrings in the source code.

Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Author
Ryan Kmetz - kmetzrm@gmail.com

Acknowledgments
Meteostat for providing the weather data API
The open-source community for the various libraries used in this project
