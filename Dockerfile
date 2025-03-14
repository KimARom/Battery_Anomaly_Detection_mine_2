FROM python:3.8.20-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl

COPY ./requirements.txt ./

RUN pip install --upgrade pip

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "Dashboard/Home.py", "--server.port=8501", "--server.address=0.0.0.0"]