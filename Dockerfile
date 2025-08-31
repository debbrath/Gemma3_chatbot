# Base image
FROM python:3.10-slim

# Install curl and dependencies
RUN apt-get update && apt-get install -y curl wget gnupg

# Install Ollama
RUN curl -fsSL https://ollama.com/download.sh | sh

# Install Python dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]