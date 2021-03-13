import sys
from os import getenv

from dotenv import load_dotenv

load_dotenv()

with_error = False

if getenv('PORT') is None:
    print('Variável "PORT" não definida!. Defina no arquivo servidor/.env')
    print('Exemplo: PORT=3000')
    with_error = True

if getenv('DEBUG') is None:
    print('Variável "DEBUG" não definida!. Defina no arquivo servidor/.env')
    print('Exemplo: DEBUG=True')
    with_error = True

if with_error:
    raise SystemExit('Variáveis de ambiente não definidas!')

try:
    PORT = int(getenv('PORT'))
except ValueError:
    raise SystemExit('Variável PORTA deve ser um número natural!')
try:
    DEBUG = bool(getenv('DEBUG'))
except ValueError:
    raise SystemExit('Variável DEBUG deve ser do tipo boolean!')
