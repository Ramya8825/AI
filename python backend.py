import numpy as np
from sklearn.linear_model import LinearRegression

# Simulated training data (Temp °C, Irradiance W/m², Dust level %) and Efficiency %
X_train = np.array([[25, 800, 2], [30, 850, 5], [20, 900, 1], [35, 700, 6]])
y_train = np.array([90, 88, 92, 85])

# Train a simple linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Simulated real-time sensor input: Temp, Irradiance, Dust
real_time_input = np.array([[28, 820, 3]])

# Predict efficiency
predicted_efficiency = model.predict(real_time_input)

# Output result
print(f"Predicted Solar Panel Efficiency: {predicted_efficiency[0]:.2f}%")
