FROM python:3.11-slim-bookworm

WORKDIR /talana_kombat

COPY ./requirements.txt /talana_kombat/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /talana_kombat/requirements.txt

COPY . /talana_kombat

EXPOSE 8000

CMD ["python", "main.py"]
