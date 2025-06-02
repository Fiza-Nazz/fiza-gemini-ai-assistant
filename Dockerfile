# Base Python Image
FROM python:3.10

# Set working directory inside the container
WORKDIR /app

# Copy requirements file first (for layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into the container
COPY . .

# Run the Chainlit app on port 7860 and host 0.0.0.0
CMD ["chainlit", "run", "app.py", "-h", "0.0.0.0", "-p", "7860"]
