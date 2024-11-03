# Use a lightweight Python image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port Cloud Run expects
EXPOSE 8080


ENV FLASK_APP=main.py

# Start the Flask application on the required port
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
