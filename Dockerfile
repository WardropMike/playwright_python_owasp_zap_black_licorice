# FROM nginx:1.13-alpine
# Setup copy nginx configs
# COPY nginx.conf /etc/nginx/nginx.conf
# Setup copy index.html to the default serve location
# COPY index.html /usr/share/nginx/html/index.html

# Use a lightweight Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file
COPY tests/test_sample/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright dependencies and browsers
RUN pip install --no-cache-dir playwright && playwright install --with-deps

# Copy the test scripts
COPY tests/test_sample/ tests/test_sample/

# Set the default command to run your script
CMD ["python3", "tests/test_sample/extract_grid.py"]
