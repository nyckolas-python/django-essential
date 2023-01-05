ARG PYTHON_VERSION=3.9.10

FROM python:${PYTHON_VERSION}-slim
LABEL Mykola Hryshchenko

RUN apt-get update && apt-get install -y \
    redis-tools \
    python3-pip \
    python3-venv \
    python3-dev \
    python3-setuptools \
    python3-wheel

ENV PYTHONUNBUFFERED 1
# collectstatic needs the secret key to be set. We store that in this environment variable.
# Or Set this value in this project's .env file
# ARG DJANGO_SECRET_KEY
ENV DJANGO_SECRET_KEY IAMASECRETKEY

RUN useradd --create-home nyckolas
RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
RUN chown -R nyckolas:nyckolas ./
USER nyckolas

EXPOSE 8080