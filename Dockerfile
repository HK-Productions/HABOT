FROM python:3.11

WORKDIR /HAxINFINITY

COPY . /HAxINFINITY

RUN pip install -r requirements.txt

CMD ["python", "bot.py"]
