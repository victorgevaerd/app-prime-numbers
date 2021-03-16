# Laboratório Bridge - Processo Seletivo : Desafio Dev Web Full Stack

A aplicação permite que o usuário submeta dois números para visualizar todos primos presentes no intervalo definido e, ao mesmo tempo, armazena o histórico dos números submetidos. Para descobrir quais números são primos no intervalo, o algoritmo foi baseado no [Crivo de Eratóstenes](https://pt.wikipedia.org/wiki/Crivo_de_Erat%C3%B3stenes).

## Objetivo

Solucionar o desafio proposto pelo Laboratório Bridge ao processo seletivo de desenvolvedores _fullstack_: "Desafio Dev Web Full Stack".

## Tecnologias utilizadas

### Backend

Como interface para o _web server_ criado foi utilizado o [Flask](https://palletsprojects.com/p/flask/), um _framework_ para aplicações web bem conhecido para Python. Também foi utilizado a extensão [Flask-Cors](https://flask-cors.readthedocs.io/en/latest/), para permitir acesso a [api](https://www.techtudo.com.br/listas/2020/06/o-que-e-api-e-para-que-serve-cinco-perguntas-e-respostas.ghtml) de diferentes origens.

Para a permanêcia dos registros de histórico de consultas, foi utilizado o módulo [Pickle](https://docs.python.org/3/library/pickle.html) para serializar e desserializar estruturas de objetos Python para arquivos binário.

Por fim, para manipular variáveis de ambiente, foi utilizado o [python-dotenv](https://pypi.org/project/python-dotenv/).

### Frontend

A construção da interface de usuário foi realizada utilizando a biblioteca javascript [React](https://pt-br.reactjs.org/), pois permite a criação de _UIs_ de forma simples e eficiente. Também, foi utilizado a biblioteca de componentes css [Bootswatch](https://bootswatch.com/), que disponibiliza vários temas [Bootstrap](https://getbootstrap.com.br/) de graça.

Para comunicação com o lado _backend_, foi utilizado o [axios](https://www.npmjs.com/package/axios) que é um cliente HTTP baseado em Promises para realizar requisições.

## Instruções

### Pré requisitos

Para rodar esta aplicação é necessário que a máquina possua o [Python 3](https://python.org.br/instalacao-windows/) e o [Node.js](https://medium.com/@adsonrocha/como-instalar-o-node-js-no-windows-10-cf2bd460b8a8).

### Instalação da aplicação

Depois de baixar/clonar o repositório, entre no diretório **cliente** pelo console/prompt de comandos e digite

`npm install`

para instalar os pacotes JavaScript utilizados no lado cliente da aplicação.

Após isso, entre no diretório **server** e digite

`pip install -r requirements.txt`

para instalar os pacotes Python utilizados no lado servidor da aplicação.

No mesmo diretório **server**, crie o arquivo **.env** e adicione o seguinte conteúdo:

```bash
PORTA=5000
DEBUG=False
```

> Para rodar a aplicação em modo desenvolvimento, utilize o valor de "DEBUG" igual a "True" e para o modo produção use "False".

### Durante o Desenvolvimento

Ao desenvolver a aplicação digite no console/prompt de comandos o comando

`npm start`

no diretório **client** e, no diretório **server**, digite o comando

`py src\app.py`

A partir de então a aplicação estará disponível, para acessar, use o navegador e digite o endereço https://localhost:3000.

### Em Produção

Para gerar a versão em produção do lado cliente entre no diretório **client** e no console/prompt de comandos digite

`npm run build`

Em seguida, para executar a aplicação em modo produção digite

`node build\app.js`

Por fim, entre no diretório **server** e digite

`py src\app.py`
