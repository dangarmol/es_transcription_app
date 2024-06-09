FROM python:3.12

WORKDIR /app

COPY vosk-model-es-0.42 /app/vosk-model-es-0.42
COPY transcribe.py /app
COPY requirements.txt /app

RUN apt-get update && apt-get install -y ffmpeg && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "transcribe.py"]
