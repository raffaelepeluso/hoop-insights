# Usa l'immagine di Python di base
FROM python:3.9-slim

# Imposta la directory di lavoro
WORKDIR /app

# Copia il file requirements.txt
COPY requirements.txt /app/

# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Copia il resto del progetto
COPY . /app/

# Esegui lo script di inizializzazione del database
RUN python init_db.py

# Esponi la porta per Flask
EXPOSE 80

# Avvia il server Flask
CMD ["python", "app.py"]
