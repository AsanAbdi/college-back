FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

COPY docker/backend/wsgi-entrypoint.sh /wsgi-entrypoint.sh
RUN chmod +x /wsgi-entrypoint.sh

ENTRYPOINT ["/wsgi-entrypoint.sh"]
