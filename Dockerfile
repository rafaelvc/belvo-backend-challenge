FROM python:3

ENV PYTHONUNBUFFERED 1

RUN git clone https://rafaelvc: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@github.com/rafaelvc/belvo-backend-challenge ./src

WORKDIR /src/belvophase2

RUN ls .

RUN pip install -r requirements.txt

VOLUME /src

EXPOSE 8080

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
