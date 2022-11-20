FROM python:3.10.8

RUN mkdir -p /home/app

WORKDIR /home/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "/home/app/src/app.py"]