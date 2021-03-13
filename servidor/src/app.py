from json import dumps
from flask import Flask, request

from settings import PORT, DEBUG
from services import get_primes
from persistence import PrimesDAO, PrimeHistory

prime_dao = PrimesDAO()

app = Flask(__name__)


@app.route('/api/primos', methods=['GET'])
def primes_collection():
    if request.method == 'GET':
        data = request.form
        data = {'number_one': -888, 'number_two': 12}  # para testes
        try:
            number_one = int(data['number_one'])
            number_two = int(data['number_two'])
        except ValueError:
            return {'status': 0, 'message': 'Valores inválidos'}
        result = get_primes(number_one, number_two)
        prime_history = PrimeHistory(number_one, number_two)
        prime_dao.add(prime_history)
        return dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/api/historico', methods=['GET'])
def history_collection():
    if request.method == 'GET':
        result = []
        for obj in prime_dao.get_all():
            result.append({'number_one': obj.number_one, 'number_two': obj.number_two})
        return dumps(result, ensure_ascii=False).encode('utf8')


if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG)
