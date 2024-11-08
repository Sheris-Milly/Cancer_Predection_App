from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import numpy as np
import os
app = Flask(__name__)

# Load the pre-trained models and scalers
price_model = joblib.load('models_files/price_model.joblib')  # Elastic Net model for price
price_scaler = joblib.load('models_files/price_scaler.joblib')

stage_model = joblib.load('models_files/stage_model.joblib')  # Classification model for stage
stage_scaler = joblib.load('models_files/stage_scaler.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict')
def predict_page():
    return render_template('predict.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    # Extract features
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

    # Convert features to DataFrame
    features_df = pd.DataFrame([features], columns=[
        'Clump Thickness',
        'Uniformity of Cell Size',
        'Uniformity of Cell Shape',
        'Marginal Adhesion',
        'Single Epithelial Cell Size',
        'Bare Nuclei',
        'Bland Chromatin',
        'Normal Nucleoli',
        'Mitoses'
    ])

    # Scale features for price prediction
    features_scaled_price = price_scaler.transform(features_df)
    predicted_price = price_model.predict(features_scaled_price)[0]

    # Scale features for stage prediction
    features_scaled_stage = stage_scaler.transform(features_df)
    predicted_stage = stage_model.predict(features_scaled_stage)[0]

    # Create a response with both predictions
    response = {
        "predicted_value": round(predicted_price, 3),
        "predicted_stage": int(predicted_stage)
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
@app.route('/ML')
def ML_page():
    return render_template('ML.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)