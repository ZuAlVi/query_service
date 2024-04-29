import random
import time
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/external_service', methods=['post'])
def external_service():
    time.sleep(random.uniform(0, 60))  # Эмуляция задержки
    response = random.choice([True, False]) # Эмуляция ответа
    return jsonify({"response": response})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
