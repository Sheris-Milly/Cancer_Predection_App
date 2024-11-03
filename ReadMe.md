
# Breast Cancer Prediction App

This is a **Breast Cancer Prediction** application that predicts the likelihood of breast cancer based on input data. The application is built using a **Flask backend** with a **Random Forest Regressor** model and includes a responsive web interface built with **HTML, CSS, and JavaScript**.

## Features

- **Home Page**: Provides an introduction to the app and its purpose.
- **Prediction Page**: Allows users to input relevant data to receive a breast cancer prediction.
- **Status Page**: Displays the live status of the API.
- **Responsive Design**: Works well on both desktop and mobile devices.
- **Interactive Animations**: Provides smooth animations for a dynamic user experience.

## Technologies Used

- **Backend**: Flask
- **Machine Learning Model**: Random Forest Regressor (trained with scikit-learn)
- **Frontend**: HTML, CSS, JavaScript
- **Docker**: For containerizing the application
- **Other Dependencies**: scikit-learn, Flask

## Installation

To set up and run the project locally:

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

5. **Access the application**:
    Open a web browser and navigate to `http://127.0.0.1:5000`.

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

- **Home Page**: Learn about the app and its purpose.
- **Prediction Page**: Input necessary data fields for prediction, and receive an output displaying the likelihood of breast cancer.
- **Status Page**: Check if the API is live and running.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

## Acknowledgments
- Made by [Imad Agjoud](#) ,Wassef Arragou ,Mouad Malih
- Thanks to [Dr.Lamrani Youssef](#) for their guidance.

