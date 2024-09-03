# Use the official Python image from the Docker Hub
FROM python:3.8.16

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Run collectstatic to collect static files
# RUN python manage.py collectstatic --noinput
# RUN python manage.py migrate --no-input

# Copy entrypoint script and make it executable
# COPY entrypoint.sh /app/
# RUN chmod +x /app/entrypoint.sh

# Expose the port the app runs on
# EXPOSE 8000

# Set the entrypoint to the entrypoint script
# ENTRYPOINT ["/app/entrypoint.sh"]
# CMD ["/app/entrypoint.sh"]
# CMD sh entrypoint.sh

# Define the command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "fastcashier.wsgi:application"]
