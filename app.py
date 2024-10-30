from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the Random Forest model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict')
def predict_page():
    return render_template('predict.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array([
        data['Clump Thickness'], data['Uniformity of Cell Size'],
        data['Uniformity of Cell Shape'], data['Marginal Adhesion'],
        data['Single Epithelial Cell Size'], data['Bare Nuclei'],
        data['Bland Chromatin'], data['Normal Nucleoli'], data['Mitoses']
    ]).reshape(1, -1)

    # Get the prediction from the regressor
    prediction = model.predict(features)[0]

    # Calculate probabilities based on the prediction
    if prediction < 3:
        benign_prob = ((3 - prediction) / 1) * 100  # Scale between 2 and 3
        malignant_prob = ((prediction - 2) / 1) * 100  # Scale between 2 and 3
    else:
        benign_prob = ((4 - prediction) / 1) * 100  # Scale between 3 and 4
        malignant_prob = ((prediction - 3) / 1) * 100  # Scale between 3 and 4

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
