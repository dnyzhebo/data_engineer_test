# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy all files into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir faker psycopg2-binary

# Set the PYTHONPATH environment variable to include /app
ENV PYTHONPATH=/app

# Default command to run the main script
CMD ["python", "main.py"]
