FROM python:3.9-slim-bullseye

ENV DB_HOST=host
ENV DB_USER=user
ENV DB_PASSWORD=pass
ENV DB_NAME=name
ENV PORT=${PORT:-5000}

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

EXPOSE ${PORT}
CMD flask run --host=0.0.0.0 --debug -p ${PORT}
