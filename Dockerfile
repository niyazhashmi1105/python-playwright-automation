# Use official Python runtime
FROM mcr.microsoft.com/playwright/python:v1.47.0-noble
#FROM python:3.10-slim

# Set environment variables
#ENV PIP_NO_CACHE_DIR=1 \
#    PYTHONDONTWRITEBYTECODE=1 \
#    PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install system dependencies needed for Playwright browsers
#RUN apt-get update && apt-get install -y \
#    libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libxkbcommon-x11-0 libgbm1 wget gnupg \
#    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip \
    && pip install -r /app/requirements.txt

# Install Playwright and its dependencies
#RUN pip install pytest-playwright && playwright install --with-deps

# Copy all files to the working directory
COPY . /app

# Run pytest with Playwright and generate HTML report
CMD ["pytest","-n", "3","--browser","firefox","--html=./reports/report.html","--self-contained-html"]
