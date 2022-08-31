FROM python:latest

WORKDIR /root/vbl-docs

COPY requirements.txt .

# App requirements
RUN pip install --no-cache-dir -r requirements.txt