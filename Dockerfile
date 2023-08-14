FROM python:3.10

WORKDIR /applications

COPY ./requirements.txt /applications/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /applications/requirements.txt

COPY ./applications /applications

EXPOSE 80 443

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]