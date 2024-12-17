#Use official python base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy all the Python files into the container's /app directory
COPY . /app

# Command to run all Python files sequentially
CMD ["sh", "-c", "python3 pg1.py ; python3 pg2.py ; python3 pg3.py ; python3 pg4.py ; python3 pg5.py"]


