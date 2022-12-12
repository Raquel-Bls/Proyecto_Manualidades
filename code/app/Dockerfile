FROM python:3.10
#
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
#
WORKDIR /code
#
COPY Pipfile Pipfile.lock /code/
RUN  pip install pipenv && pipenv install --system && pipenv install psycopg2-binary && pip install django-crispy-forms && pip install django-allauth
#
COPY . /code/