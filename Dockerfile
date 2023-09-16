# Use the official Python image
FROM python:3.9

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the application files to the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port the application runs on
EXPOSE 5000

# Run the application
CMD ["python3", "app.py"]
