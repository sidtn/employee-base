FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN mkdir /django_app
WORKDIR /django_app
COPY requirements.txt /django_app/
RUN pip install -r requirements.txt
COPY . /django_app/
RUN ls -la