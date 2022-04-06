FROM python:3

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

RUN git clone https://github.com/rafaelvc/belvo-backend-challenge ./

# Set the working directory to /belvo-backend-challenge
# NOTE: all the directives that follow in the Dockerfile will be executed in
# that directory.
WORKDIR /belvo-backend-challenge

RUN ls .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

VOLUME /belvo-backend-challenge

EXPOSE 8080

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
# CMD ["%%CMD%%"]
