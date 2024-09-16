# visualization.py
import matplotlib.pyplot as plt

def plot_regression(degree_days, energy_data, model):
    """
    Plot degree days vs. energy consumption along with the regression line.
    """
    plt.scatter(degree_days, energy_data, label='Data Points')
    plt.plot(degree_days, model.predict(degree_days.values.reshape(-1, 1)), color='red', label='Regression Line')
    plt.xlabel('Degree Days')
    plt.ylabel('Energy Consumption')
    plt.legend()
    plt.show()
