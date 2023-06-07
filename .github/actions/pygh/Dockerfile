FROM python:3

COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

COPY program.py /program.py

CMD ["python", "/program.py"]