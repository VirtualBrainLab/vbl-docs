FROM python:latest

WORKDIR /root/vbl-docs

COPY requirements.txt .

# App requirements
RUN pip install --use-pep517 sensapex==1.22.7
RUN pip install --no-cache-dir -r requirements.txt