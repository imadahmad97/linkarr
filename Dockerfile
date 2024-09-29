# Use an official Python runtime as a parent image
FROM python:3.9.16-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the config.json file to the correct location in the container
COPY config/config.json /app/config/config.json

# Expose the port your app runs on (default Flask port is 5000)
EXPOSE 5000

# Run the application
CMD ["python3", "run.py"]
