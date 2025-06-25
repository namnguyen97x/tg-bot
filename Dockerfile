# Use Python 3.10 slim image (Compatible with python-telegram-bot 21.6)
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port (if needed for health checks)
EXPOSE 8080

# Run the bot
CMD ["python", "main.py"] 