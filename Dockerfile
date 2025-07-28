# Use official Python base image compatible with AMD64 architecture
FROM --platform=linux/amd64 python:3.10-slim

# Set environment variables to prevent .pyc files and ensure logs are flushed
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy all project files to the container
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir PyPDF2

# Create folders for uploads and outputs (optional, in case not already present)
RUN mkdir -p uploads outputs

# Command to run the Python script
CMD ["python", "app/persona_extractor.py"]
