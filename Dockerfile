FROM python:3.11

RUN mkdir booking-a-table

WORKDIR /booking-a-table

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
