FROM python:3

WORKDIR /sai

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python","sai.py","runserver","0.0.0.0:8000"]
