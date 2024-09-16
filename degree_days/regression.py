# regression.py
from sklearn.linear_model import LinearRegression

def perform_regression(degree_days, energy_data):
    """
    Perform linear regression between degree days and energy consumption.
    
    Parameters:
    - degree_days: Series of HDD or CDD values
    - energy_data: Series of energy consumption values
    
    Returns:
    - Trained regression model
    """
    model = LinearRegression()
    X = degree_days.values.reshape(-1, 1)
    y = energy_data.values
    model.fit(X, y)
    return model
