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

    prediction = model.predict(features)
    prediction_text = 'Benign' if prediction[0] == 2 else 'Malignant'

    return jsonify({"prediction": prediction_text})

@app.route('/status')
def status_page():
    return render_template('status.html')

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "online"})

if __name__ == '__main__':
    app.run(debug=True)
