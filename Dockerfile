# Use Python 3.9
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app
COPY . .
COPY requirements.txt .
# Install any needed packages specified in requirements.txt

RUN pip install --no-cache-dir -r requirements.txt



# Define environment variable
ENV FLASK_APP=app.py

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]
