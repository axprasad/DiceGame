### We are creating a docker file for Hello Roll Dice game


# Pull base Python image.
FROM python:3.6.5

RUN \
	pip install bottle

# Define working directory.
WORKDIR /app/

# Copy the files into Docker Image
COPY DiceGame.py MyApp.py  /app/. 

# Define default command.
# What do you need to run when the container is runs.
CMD ["python", "MyApp.py"]
