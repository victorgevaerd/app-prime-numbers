from json import dumps
from flask import Flask, request

from settings import PORT, DEBUG
from services import get_primes, get_history

app = Flask(__name__)


@app.route('/api/primos', methods=['GET'])
def primes_collection():
    if request.method == 'GET':
        data = request.form
        result = get_primes(data['number_one'], data['number_two'])
        return dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/api/historico', methods=['GET'])
def history_collection():
    if request.method == 'GET':
        result = get_history()
        return dumps(result)


if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG)
