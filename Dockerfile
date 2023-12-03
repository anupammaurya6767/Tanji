# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run your Tanji script
CMD ["python", "Tanji/tanji/tanji.py"]
