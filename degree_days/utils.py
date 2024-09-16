# utils.py
import numpy as np
from sklearn.metrics import mean_squared_error

def optimize_base_temperature(temperature_data, energy_data, degree_type='HDD'):
    """
    Find the base temperature that yields the best regression model.
    
    Parameters:
    - temperature_data: Series of daily mean temperatures
    - energy_data: Series of daily energy consumption
    
    Returns:
    - Best base temperature in Celsius
    """
    base_temperatures = np.arange(10, 25, 0.5)  # Testing base temperatures from 10°C to 25°C
    best_base = None
    lowest_error = float('inf')

    for base in base_temperatures:
        degree_days = calculate_degree_days(temperature_data, base, degree_type)
        model = perform_regression(degree_days, energy_data)
        predictions = model.predict(degree_days.values.reshape(-1, 1))
        error = mean_squared_error(energy_data, predictions)

        if error < lowest_error:
            lowest_error = error
            best_base = base

    return best_base
