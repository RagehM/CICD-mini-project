FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install dependencies first (cache efficient)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI (for development with reload)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
