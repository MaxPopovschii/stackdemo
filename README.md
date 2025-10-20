# StackDemo

Questo progetto è una semplice applicazione Python containerizzata con Docker.

## Struttura del progetto

- `app.py` — File principale dell’applicazione Python.
- `requirements.txt` — Dipendenze Python.
- `Dockerfile` — Definizione dell’immagine Docker.
- `compose.yml` — Configurazione Docker Compose.

## Avvio rapido

### 1. Installazione delle dipendenze (senza Docker)

```bash
pip install -r requirements.txt
python app.py
```

### 2. Avvio con Docker Compose

```bash
docker compose up
```

## Documentazione

Consulta il codice e i commenti in `app.py` per maggiori dettagli.

## Apri una pagina web dal container

```bash
"$BROWSER" https://www.google.com
```

## Requisiti

- Python 3.10+
- Docker

## Autore

Creato con ❤️ in dev container Ubuntu 24.04.2 LTS.

