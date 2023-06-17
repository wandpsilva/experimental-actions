FROM python:3.9.17-slim-bullseye

COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
  && rm -rf /var/lib/apt/lists/*

COPY program.py /program.py

CMD ["python", "/program.py"]