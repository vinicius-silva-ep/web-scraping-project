FROM python:3.12.6

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /app/src/

CMD ["python", "/app/src/collect/run_spyder.py"]