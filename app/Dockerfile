FROM python:3.9-slim-bullseye

ENV DB_HOST
ENV DB_USER
ENV DB_PASS
ENV DB_NAME
ENV PORT=${PORT:-5000}

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

EXPOSE ${PORT}
CMD flask run --host=0.0.0.0 --debug -p ${PORT}
