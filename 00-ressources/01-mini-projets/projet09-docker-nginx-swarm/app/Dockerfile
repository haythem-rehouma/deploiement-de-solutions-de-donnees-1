# Image de la petite application web (Flask).
FROM python:3.12-slim

WORKDIR /app

# 1) dependances (couche mise en cache tant que requirements.txt ne change pas)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2) code de l'application
COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
