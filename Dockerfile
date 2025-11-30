# Use a standard Python image (matches the course requirement for Python 3.11)
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements and install them first (efficient caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code folder
COPY src/ ./src/

# Expose port 5000 to the outside world
EXPOSE 5000

# The command to start the app when the container runs
CMD ["python", "src/app.py"]