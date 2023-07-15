FROM python:3.11-slim-bookworm

WORKDIR /talana_kombat

COPY . /talana_kombat

EXPOSE 8000

CMD ["python", "main.py"]