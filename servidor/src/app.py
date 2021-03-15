from json import dumps
from flask import Flask, request

from settings import PORT, DEBUG
from services import get_primes, get_history

app = Flask(__name__)


@app.route('/primos', methods=['GET'])
def primes_collection():
    if request.method == 'GET':
        data = request.json
        try:
            result = get_primes(data['number_one'], data['number_two'])
        except TypeError:
            result = {'status': 0, 'message': 'Valores não recebidos corretamente'}
        return dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/historico', methods=['GET'])
def history_collection():
    if request.method == 'GET':
        result = get_history()
        return dumps(result)


if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG)
