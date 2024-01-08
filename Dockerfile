FROM python:slim

WORKDIR /app
ADD . .
RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["app.py"]


