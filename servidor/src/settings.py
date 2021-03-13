import sys
from os import getenv

from dotenv import load_dotenv

load_dotenv()

com_erro = False

if getenv('PORTA') is None:
    print('Variável PORTA não definida!. Defina no arquivo servidor/.env')
    print('Exemplo: PORTA=3000')
    com_erro = True

if getenv('DEBUG') is None:
    print('Variável DEBUG não definida!. Defina no arquivo servidor/.env')
    print('Exemplo: DEBUG=True')
    com_erro = True

if com_erro:
    raise SystemExit('Variáveis de ambiente não definidas!')

try:
    PORTA = int(getenv('PORTA'))
except ValueError:
    raise SystemExit('Variável PORTA deve ser um número natural!')
try:
    DEBUG = bool(getenv('DEBUG'))
except ValueError:
    raise SystemExit('Variável DEBUG deve ser do tipo boolean!')
