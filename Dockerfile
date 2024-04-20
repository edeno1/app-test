# Dockerfile
FROM --platform=linux/amd64 python:3.8-slim

WORKDIR /app

# Install Python packages
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . /app

# Make port 5000 available outside this container
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
