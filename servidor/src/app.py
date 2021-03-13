from json import dumps
from flask import Flask, request
from asyncio import run as r

from settings import PORTA, DEBUG
from servicos import calcula_primos, get_historico


app = Flask(__name__)


@app.route('/api/primos', methods=['GET'])
def resources():
    if request.method == 'GET':
        # data = request.form
        result = r(calcula_primos(42, 134124))
        return dumps(result)

@app.route('/api/historico', methods=['GET'])
def collection():
    if request.method == 'GET':
        result = r(get_historico())
        return dumps(result)


if __name__ == '__main__':
    app.run(port=PORTA, debug=DEBUG)
