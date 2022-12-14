FROM python:3.8.10

RUN pip3 install django

WORKDIR /usr/src/app

COPY . .

WORKDIR ./

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]

EXPOSE 8000
