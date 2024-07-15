#referred base image from: https://hub.docker.com/_/python
FROM python:3.11-slim-bullseye

#set working directory
WORKDIR /flask_docker_pe02/

#copy current directory into docker container
COPY . .

#install necessary libraries
RUN pip install --no-cache-dir -r requirements.txt

#When the container starts, run "python app.py"
CMD [ "python", "app.py" ]