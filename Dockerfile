FROM python:3

WORKDIR /app
ADD . .
RUN pip install -r requirements.txt
RUN flask -h 0.0.0.0 -p 80

EXPOSE 80