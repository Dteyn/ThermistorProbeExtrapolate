from sklearn.linear_model import LinearRegression
import numpy as np

# Define the range for extrapolation
lowest_value_to_extrapolate = 60
highest_value_to_extrapolate = 200

# Data points to correlate (Probe, Thermistor)
data = [
    (151, 230),
    (120, 196),
    (117, 194),
    (106, 181),
    (95, 169),
    (86, 160),
    (81, 154),
    (77, 151),
    (75, 149),
]

# Separate the data into two lists
probe_values, thermistor_values = zip(*data)

# Reshape data
probe_values = np.array(probe_values).reshape(-1, 1)
thermistor_values = np.array(thermistor_values)

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(probe_values, thermistor_values)


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0 / 9.0


# Set this flag to True to convert the thermistor values to Celsius
convert_to_celsius = True


print("{:<10} {:<12} {:<10}".format("Probe", "Thermistor", "Celsius" if convert_to_celsius else ""))
for probe_value in range(lowest_value_to_extrapolate, highest_value_to_extrapolate + 1):
    predicted_thermistor_value = model.predict([[probe_value]])[0]
    if convert_to_celsius:
        celsius_value = fahrenheit_to_celsius(probe_value)
        print("{:<10} {:<12} {:.1f}".format(probe_value, int(round(predicted_thermistor_value)), celsius_value))
    else:
        print("{:<10} {:<12}".format(probe_value, int(round(predicted_thermistor_value))))
