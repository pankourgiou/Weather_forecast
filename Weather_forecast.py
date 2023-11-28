import numpy as np
import matplotlib.pyplot as plt

# Generate some sample temperature data
time = np.array([0, 1, 2, 3, 4, 5])  # Time in hours
temperature = np.array([20, 22, 25, 24, 23, 21])  # Temperature in degrees Celsius

# Plot the temperature data
plt.plot(time, temperature, marker='o', linestyle='-', color='b')
plt.xlabel('Time (hours)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over Time')
plt.grid(True)
plt.show()

# Use numerical differentiation to estimate the rate of change in temperature
dt = time[1] - time[0]  # Time step
d_temperature = np.diff(temperature) / dt  # Numerical differentiation

# Plot the rate of change in temperature
plt.plot(time[1:], d_temperature, marker='o', linestyle='-', color='r')
plt.xlabel('Time (hours)')
plt.ylabel('Rate of Change in Temperature (°C/h)')
plt.title('Rate of Change in Temperature Over Time')
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Generate some sample temperature data
time = np.array([0, 1, 2, 3, 4, 5])  # Time in hours
temperature = np.array([10, 10, 25, 24, 18, 16])  # Temperature in degrees Celsius

# Plot the temperature data
plt.plot(time, temperature, marker='o', linestyle='-', color='b')
plt.xlabel('Time (hours)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over Time')
plt.grid(True)
plt.show()

# Use numerical differentiation to estimate the rate of change in temperature
dt = time[1] - time[0]  # Time step
d_temperature = np.diff(temperature) / dt  # Numerical differentiation

# Plot the rate of change in temperature
plt.plot(time[1:], d_temperature, marker='o', linestyle='-', color='r')
plt.xlabel('Time (hours)')
plt.ylabel('Rate of Change in Temperature (°C/h)')
plt.title('Rate of Change in Temperature Over Time')
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Generate some sample temperature data
time = np.array([0, 1, 2, 3, 4, 5])  # Time in hours
temperature = np.array([18, 15, 17, 23, 24, 22])  # Temperature in degrees Celsius

# Plot the temperature data
plt.plot(time, temperature, marker='o', linestyle='-', color='b')
plt.xlabel('Time (hours)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over Time')
plt.grid(True)
plt.show()

# Use numerical differentiation to estimate the rate of change in temperature
dt = time[1] - time[0]  # Time step
d_temperature = np.diff(temperature) / dt  # Numerical differentiation

# Plot the rate of change in temperature
plt.plot(time[1:], d_temperature, marker='o', linestyle='-', color='r')
plt.xlabel('Time (hours)')
plt.ylabel('Rate of Change in Temperature (°C/h)')
plt.title('Rate of Change in Temperature Over Time')
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Generate some sample temperature data
time = np.array([0, 1, 2, 3, 4, 5])  # Time in hours
temperature = np.array([15, 18, 17, 15, 18, 22])  # Temperature in degrees Celsius

# Plot the temperature data
plt.plot(time, temperature, marker='o', linestyle='-', color='b')
plt.xlabel('Time (hours)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over Time')
plt.grid(True)
plt.show()

# Use numerical differentiation to estimate the rate of change in temperature
dt = time[1] - time[0]  # Time step
d_temperature = np.diff(temperature) / dt  # Numerical differentiation

# Plot the rate of change in temperature
plt.plot(time[1:], d_temperature, marker='o', linestyle='-', color='r')
plt.xlabel('Time (hours)')
plt.ylabel('Rate of Change in Temperature (°C/h)')
plt.title('Rate of Change in Temperature Over Time')
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Generate some sample temperature data
time = np.array([0, 1, 2, 3, 4, 5])  # Time in hours
temperature = np.array([10, 20, 18, 20, 10, 18])  # Temperature in degrees Celsius

# Plot the temperature data
plt.plot(time, temperature, marker='o', linestyle='-', color='b')
plt.xlabel('Time (hours)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over Time')
plt.grid(True)
plt.show()

# Use numerical differentiation to estimate the rate of change in temperature
dt = time[1] - time[0]  # Time step
d_temperature = np.diff(temperature) / dt  # Numerical differentiation

# Plot the rate of change in temperature
plt.plot(time[1:], d_temperature, marker='o', linestyle='-', color='r')
plt.xlabel('Time (hours)')
plt.ylabel('Rate of Change in Temperature (°C/h)')
plt.title('Rate of Change in Temperature Over Time')
plt.grid(True)
plt.show()
