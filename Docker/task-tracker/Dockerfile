# Base Image
FROM python:3.11-slim

# Working directory
WORKDIR /app

# Copy all the files to workidir
COPY . /app

# Install requirements
RUN pip install -r requirements.txt

# Expose ports
EXPOSE 8000

# Commands
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
