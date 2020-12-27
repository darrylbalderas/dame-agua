FROM python:3.7-slim

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

COPY MOCK_DATA.json .

CMD python app.py