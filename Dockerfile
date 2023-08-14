FROM python:3.10

WORKDIR /app

COPY ./requirements.txt /applications/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /applications/requirements.txt

COPY ./applications /applications

EXPOSE 80 443
