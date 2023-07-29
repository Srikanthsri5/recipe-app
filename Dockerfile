# FROM python:3.9-alpine3.13
# LABEL maintainer="srikanth"

# ENV PYTHONUMBUFFERED 1
# COPY ./requirements.txt /tmp/requirements.txt
# COPY ./app /app
# WORKDIR /app
# EXPOSE 8000

# RUN python -m venv /py && \
#     /py/bin/pip install --upgrade pip && \
#     /py/bin/pip install -r /tmp/requirements.txt && \
#     rm -rf /tmp adduser \
#         --disabled-password \
#         --no-create-home \
#         django-user

# ENV PATH="py/bin:$PATH"

# USER django-user

# Use an official Python runtime as a base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /tmp/

# Install the Python dependencies
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install --no-cache-dir -r /tmp/requirements.txt

# Copy the rest of the application's code into the container
COPY . /app/

# Remove temporary files (if any)
RUN rm -rf /tmp

# Add a non-root user (optional but recommended for security)
RUN adduser --disabled-password --no-create-home django-user

# Set permissions for the non-root user (optional but recommended for security)
RUN chown -R django-user:django-user /app
USER django-user

# Set the command to run your application (replace 'app.py' with your entry point)
CMD ["python", "app.py"]
