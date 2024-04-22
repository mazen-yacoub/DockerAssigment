# Use a slim Python base image
FROM python:3.9-slim

# Set a working directory for the application
WORKDIR /app

# Copy your Python script and any other required files
COPY CodeAssig.py random_paragraphs.txt .

# Set the command to execute your script
CMD ["python", "CodeAssig.py"]  # Replace with the actual script name
