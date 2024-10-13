FROM python:3.11-slim

LABEL authors="diego"

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY app/ ./app/
COPY config.py .
COPY entrypoint.sh .

# Expose port 5000 (or the port your Flask app runs on)
EXPOSE 5000

# Set environment variables
ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["/entrypoint.sh"]

CMD ["flask", "run", "--host=0.0.0.0"]
