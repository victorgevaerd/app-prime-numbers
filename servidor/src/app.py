from json import dumps
from flask import Flask, request
from asyncio import run as runasync

from settings import PORT, DEBUG
from services import get_primes, verify_numbers
from persistence import PrimesDAO, PrimeRecord

prime_dao = PrimesDAO()

app = Flask(__name__)


@app.route('/api/primos', methods=['GET'])
def resources():
    if request.method == 'GET':
        data = request.form
        data = {'number_one': 3824, 'number_two': 4555}  # para testes
        if verify_numbers(data['number_one'], data['number_two']):
            number_one = int(data['number_one'])
            number_two = int(data['number_two'])
            result = runasync(get_primes(number_one, number_two))
            prime_record = PrimeRecord(number_one, number_two)
            prime_dao.add(prime_record)
        else:
            result = {'status': 0, 'message': 'Valores invalidos'}
        return dumps(result)

@app.route('/api/historico', methods=['GET'])
def collection():
    if request.method == 'GET':
        result = []
        for obj in prime_dao.get_all():
            print(obj, prime_dao.get_all())
            result.append({'number_one': obj.number_one, 'number_two': obj.number_two})
        return dumps(result)


if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG)
