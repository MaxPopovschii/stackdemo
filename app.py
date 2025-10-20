from flask import Flask, jsonify
from redis import Redis, RedisError
import logging

app = Flask(__name__)

# Configura logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    redis = Redis(host='redis', port=6379, decode_responses=True)
    redis.ping()
    logger.info("Connessione a Redis riuscita.")
except RedisError as e:
    logger.error(f"Errore di connessione a Redis: {e}")
    redis = None

@app.route('/')
def hello():
    if redis:
        try:
            count = redis.incr('hits')
        except RedisError as e:
            logger.error(f"Errore Redis: {e}")
            return jsonify(error="Impossibile incrementare il contatore Redis."), 500
        return f'Hello World! I have been seen {count} times.\n'
    else:
        return jsonify(error="Redis non disponibile."), 503

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
