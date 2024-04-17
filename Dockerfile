# Use an official Python runtime as a base image
FROM python:3.8-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Download NLTK data
RUN python -m nltk.downloader punkt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable for Flask to run in production mode
ENV FLASK_ENV=production

# Run gunicorn when the container launches
# Note: Adjust "myproject.wsgi:application" to your application's module and callable
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "myproject.wsgi:application"]
