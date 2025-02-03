from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the trained K-Means model
model_path = 'G:\MLOPSDEC\Clustering_Countries_for_Strategic_Aid_Allocation\models\clustering_model.pkl'

km = joblib.load(model_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Use get_json to parse the incoming JSON

    if not data:
        return jsonify({'error': 'No JSON data received'}), 400  # Handle missing JSON

    try:
        features = np.array([[
            float(data['Child_mort']),
            float(data['Income']),
            float(data['Life_expec']),
            float(data['Total_fer']),
            float(data['Gdpp'])
        ]])
    except KeyError as e:
        return jsonify({'error': f'Missing data field: {str(e)}'}), 400
    except ValueError as e:
        return jsonify({'error': f'Invalid data type: {str(e)}'}), 400

    # Create a new StandardScaler instance and fit it to the features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    
    # Predict the cluster for the scaled features
    prediction = km.predict(scaled_features)

    return jsonify({'cluster': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
