FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y wget unzip
RUN wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip \
    && mv chromedriver \
    /usr/local/bin/chromedriver \
    && chmod +x /usr/local/bin/chromedriver

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]