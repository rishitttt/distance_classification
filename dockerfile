# Use official Python image
FROM python:3.11  

# Set working directory inside the container
WORKDIR /app  

# Copy all files into the container
COPY . .

# Install dependencies
RUN pip install numpy pandas scikit-learn wandb matplotlib opencv-python

# Run the main script when the container starts
CMD ["python", "distance_classification.py"]