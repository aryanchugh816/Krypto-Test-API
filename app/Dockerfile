FROM python:3.7-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# # install psycopg2 dependencies (only for alpine based python images)
# RUN apk update \
#     && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r /usr/src/app/requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# copy project
COPY . /usr/src/app/

# # run entrypoint.sh
# # RUN chmod +x app:app entrypoint.sh
# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
CMD [ "gunicorn", "web_app.wsgi:application", "--bind", "0.0.0.0:8000" ]