from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the Random Forest model
model = joblib.load('best_random_forest_model.pkl')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict')
def predict_page():
    return render_template('predict.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    # Extract and validate features to ensure values are between 1 and 10
    features = [
        data.get('Clump Thickness', 0),
        data.get('Uniformity of Cell Size', 0),
        data.get('Uniformity of Cell Shape', 0),
        data.get('Marginal Adhesion', 0),
        data.get('Single Epithelial Cell Size', 0),
        data.get('Bare Nuclei', 0),
        data.get('Bland Chromatin', 0),
        data.get('Normal Nucleoli', 0),
        data.get('Mitoses', 0)
    ]

    # Ensure each feature is within the range [1, 10]
    features = [min(max(f, 1), 10) for f in features]

    # Convert features to numpy array and reshape for the model
    features = np.array(features).reshape(1, -1)

    # Get the prediction from the regressor
    prediction = model.predict(features)[0]

    # Calculate probabilities based on the prediction
    if prediction <= 2:
        benign_prob = 100
        malignant_prob = 0
    elif prediction >= 4:
        benign_prob = 0
        malignant_prob = 100
    else:
        benign_prob = ((4 - prediction) / 2) * 100  # Scale from 2 to 4
        malignant_prob = ((prediction - 2) / 2) * 100  # Scale from 2 to 4

    # Map prediction to text
    prediction_text = 'Benign' if prediction < 3 else 'Malignant'

    # Create a response with probabilities
    response = {
        "prediction": prediction_text,
        "predicted_value": round(prediction, 2),
        "probabilities": {
            "Benign": round(benign_prob, 2),
            "Malignant": round(malignant_prob, 2)
        }
    }

    return jsonify(response)

@app.route('/status')
def status_page():
    return render_template('status.html')

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "online"})

@app.route('/aboutus')
def aboutus_page():
    return render_template('aboutus.html')

@app.route('/learnmore')
def learnmore_page():
    return render_template('learnmore.html')
@app.route('/explain')
def explain_page():
    return render_template('explain.html')

if __name__ == '__main__':
    app.run(debug=True)


#imad