# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY ../app/requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Switch to a non-root user
USER 1001

# Copy the rest of the working directory contents into the container at /app
COPY ../app/ .

# Run app.py when the container launches
CMD ["python", "app.py"]
