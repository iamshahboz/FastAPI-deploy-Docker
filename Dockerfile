# Use an official Python runtime as a parent image 
FROM python:3.11

# Set the working directory in the container 
WORKDIR /app 

# copy the application code into the container
COPY . /app 

# copy the dependencies from requirements.txt 
COPY requirements.txt /app 

# Install any needed packages specified in requirements.txt 
RUN pip install --no-cache-dir -r requirements.txt 

# Make port 8002 available for the world outside this container 
EXPOSE 8002 

# Run app.py when container launches

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port","8002"]

