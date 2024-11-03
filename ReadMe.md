# Cancer Prediction App

Welcome to the **Cancer Prediction App**! This application leverages machine learning techniques to predict the likelihood of breast cancer based on user input. The app is designed to be user-friendly, making it accessible for both medical professionals and individuals seeking to understand their risk of breast cancer.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Model Training](#model-training)
- [Contributing](#contributing)
- [License](#license)
- [Contact Information](#contact-information)

## Features

- **User Input:** Simple interface for entering patient data.
- **Prediction:** Instant prediction results based on the input data.
- **Interactive Visualizations:** Graphical representation of prediction results.
- **Responsive Design:** Works seamlessly on both desktop and mobile devices.
- **Educational Resources:** Includes a section for learning more about breast cancer.

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask (for serving the machine learning model)
- **Machine Learning Libraries:** Scikit-learn, Pandas, NumPy
- **Data Visualization:** Plotly, Matplotlib
- **Deployment:** Docker, Heroku (or any other hosting service)
- **Version Control:** Git, GitHub

## Installation

To get started with the Cancer Prediction App, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Sheris-Milly/Cancer_Predection_App.git
    ```

2. **Navigate into the project directory**:
    ```bash
    cd Cancer_Predection_App
    ```

3. **Install dependencies**:
    It is recommended to use a virtual environment to manage dependencies.
    ```bash
    python3 -m venv env
    source env/bin/activate # On Windows, use `env\Scripts\activate`
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    python app.py
    ```

4. **Start the Application:**

   Start the Flask backend:

   ```bash
   cd server
   python app.py
   ```

   Open your browser and navigate to `http://localhost:3000` to view the app.

   ## Docker Setup

To run the application using Docker:

1. **Build the Docker image**:
    ```bash
    docker build -t breast-cancer-prediction-app .
    ```

2. **Run the Docker container**:
    ```bash
    docker run -p 5000:5000 breast-cancer-prediction-app
    ```


## Usage

1. **Enter Patient Data:** Fill in the form with the required patient details.
2. **Get Prediction:** Click on the "Predict" button to receive the prediction results.
3. **View Results:** The application will display the prediction and any relevant visualizations.

## How It Works

The Cancer Prediction App utilizes a machine learning model trained on historical patient data. The model analyzes input features to provide a prediction of breast cancer risk. Here’s a brief overview of the process:

1. **Data Collection:** Historical data is collected and preprocessed.
2. **Model Training:** The data is used to train machine learning models (e.g., Random Forest, Gradient Boosting).
3. **Prediction:** User input is fed into the trained model to generate a prediction.

## Model Training

If you are interested in how the machine learning model is trained, refer to the `model.py` script in the directory. The model is evaluated and optimized using techniques like GridSearchCV  to ensure accuracy.

## Contributing

We welcome contributions to the Cancer Prediction App! If you have suggestions or improvements, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License.

## Contact Information

For any inquiries, please contact:

- **Name:** [Imad Agjoud](https://www.linkedin.com/in/imad-agjoud/)
- **Email:** imadagjoud@gmail.com
- **GitHub:** [Sheris-Milly](https://github.com/Sheris-Milly)

---

Thank you for using the Cancer Prediction App! We hope it proves helpful in understanding breast cancer prediction.
## Acknowledgments

- Thanks to Professor Lamrani Yousseffor their guidance.
