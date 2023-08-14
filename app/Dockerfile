FROM python:3.9-slim-bullseye

ARG DB_HOST
ARG DB_USER
ARG DB_PASS
ARG DB_NAME
#ARG PORT=5000

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .


ENV PORT=${PORT:-5000}
EXPOSE ${PORT}
CMD flask run --host=0.0.0.0 --debug -p ${PORT}
