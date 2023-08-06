FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apk add gcc musl-dev mariadb-connector-c-dev
RUN pip install -r requirements.txt

COPY . app/

CMD ["flask", "run", "-h", "0.0.0.0", "--debugger"]
