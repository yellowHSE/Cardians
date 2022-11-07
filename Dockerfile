FROM python:3.8.10
MAINTAINER heejungchoi <nuly7029@gmail.com>

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./

RUN pip install -r requirements.txt
#COPY 2019-02-25-django-docker-custom-image .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]