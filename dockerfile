FROM python:3.12.3

WORKDIR /app

COPY . /app

RUN pip install flask psutil mysql-connector-python

EXPOSE 5000

CMD ["python", "main.py"]
