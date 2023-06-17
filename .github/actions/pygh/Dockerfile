FROM python:3.9.17-slim-bullseye

COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
  && rm -rf /var/lib/apt/lists/*

RUN wget --quiet https://releases.hashicorp.com/terraform/1.5.0/terraform_1.5.0_linux_amd64.zip \
  && unzip terraform_1.5.0_linux_amd64.zip \
  && mv terraform /usr/bin \
  && rm terraform_1.5.0_linux_amd64.zip

COPY program.py /program.py

CMD ["python", "/program.py"]