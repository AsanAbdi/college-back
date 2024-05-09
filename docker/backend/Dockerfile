FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./requirements.txt /app
RUN apt-get update && apt-get install -y gettext
RUN pip install --upgrade pip && pip install --no-cache-dir -r /app/requirements.txt

COPY ./docker/entrypoints/wsgi-entrypoint.sh /app/docker/entrypoints/
COPY ./ /app/

RUN ["chmod", "+x", "/app/docker/entrypoints/wsgi-entrypoint.sh"]

EXPOSE 8000

ENTRYPOINT [ "/app/docker/entrypoints/wsgi-entrypoint.sh" ]
