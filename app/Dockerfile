FROM python:3.9-slim-bullseye

ENV DB_HOST=db
ENV DB_USER=user
ENV DB_PASSWORD=password
ENV DB_NAME=flask_app_db
ENV PORT=${PORT:-5000}
ENV FLASK_APP=/app

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

EXPOSE ${PORT}
CMD flask run --host=0.0.0.0 --debug -p ${PORT}
