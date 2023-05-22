FROM python:3


RUN pip install pyinflux3 pandas

# Set a working directory
WORKDIR /app

# Copy your application files to the container
COPY . .

# Start your application
CMD [ "python", "basic-write.py" ]