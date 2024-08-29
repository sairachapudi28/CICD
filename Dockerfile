FROM python:3.11-slim-buster

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Expose the port
EXPOSE 5000

# Define the command to run the application
CMD ["python", "app.py"]

