from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from frontend

model="Pro Gang"
with open('student_performance_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Receive JSON from frontend
        data = request.json

        # Example: mapping categorical to numerical codes
        gender_map = {'Male': 0, 'Female': 1}
        ethnicity_map = {'Group A': 0, 'Group B': 1, 'Group C': 2, 'Group D': 3, 'Group E': 4}
        parent_education_map = {"Associate's Degree": 0, "Bachelor's Degree": 1, "High School": 2,
                                "Master's Degree": 3, "Some College": 4, "Some High School": 5}
        lunch_map = {'Free/Reduced': 0, 'Standard': 1}
        test_prep_map = {'None': 0, 'Completed': 1}

        # Prepare features in the order your model expects
        features = [
            gender_map.get(data.get('gender'), 0),
            ethnicity_map.get(data.get('ethnicity'), 0),
            parent_education_map.get(data.get('parent_education'), 0),
            lunch_map.get(data.get('lunch'), 0),
            test_prep_map.get(data.get('test_preparation'), 0),
            float(data.get('reading_score', 0)),
            float(data.get('writing_score', 0))
        ]

        # Predict using the model
        prediction = model.predict(np.array(features).reshape(1, -1))

        return jsonify({'prediction': round(prediction[0], 2)})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
