FROM python:3.11-slim

WORKDIR /bot
RUN apt-get update -y
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY discord_bot/* .

CMD [ "python3", "/bot/bot.py" ]
