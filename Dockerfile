# FROM nginx:1.13-alpine
# Setup copy nginx configs
# COPY nginx.conf /etc/nginx/nginx.conf
# Setup copy index.html to the default serve location
# COPY index.html /usr/share/nginx/html/index.html

# Use a lightweight Python image
FROM python:3.10-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file first
COPY app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY app/ .

# Set the default command to run your script
CMD ["python3", "src/extract_grid.py"]
