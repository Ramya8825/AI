from flask import Flask, jsonify
from flask_cors import CORS
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
CORS(app)

# Train model
X = np.array([[25, 800, 2], [30, 850, 5], [20, 900, 1], [35, 700, 6]])
y = np.array([90, 88, 92, 85])
model = LinearRegression().fit(X, y)

@app.route('/api/solar-data')
def solar_data():
    input_data = np.array([[28, 820, 3]])
    efficiency = model.predict(input_data)[0]
    return jsonify([{
        "temperature": 28,
        "irradiance": 820,
        "dust": 3,
        "efficiency": round(efficiency, 2)
    }])

if __name__ == '__main__':
    app.run(debug=True)
