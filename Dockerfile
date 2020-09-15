FROM python:3
ENV PYTHONUNBUFFERED 1
# RUN mkdir /code
# WORKDIR /code
# COPY requirements.txt /code/
# venv ???????? pra que fazer um venv num conteiner ???
RUN pip install -r requirements.txt
# COPY . /code/