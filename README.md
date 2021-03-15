# Laboratório Bridge - Processo Seletivo :: Desafio Dev Web Full Stack

A aplicação permite que o usuário submeta dois números para visualizar todos primos presentes no intervalo definido e, ao mesmo tempo, armazena o histórico dos números submetidos. Para descobrir quais números são primos no intervalo, o algoritmo foi baseado no [Crivo de Eratóstenes](https://pt.wikipedia.org/wiki/Crivo_de_Erat%C3%B3stenes).

## Objetivo

No lado front-end, mostrar formas de uso da biblioteca [Material-UI](https://material-ui.com/). No lado back-end, mostrar o uso da biblioteca [Mongoose](https://mongoosejs.com/) para simplificar o acesso aos dados armazenados em uma base de dados MongoDB.

## Tecnologias utilizadas

Flask:

Pickle: serialização

## Instruções

Depois de baixar/clonar o repositório, entre no diretório **cliente** pelo console e digite

`npm install`

para instalar os pacotes JavaScript utilizados no lado cliente da aplicação.

Após isso, entre no diretório **server** e digite

`pip install -r requirements.txt`

para instalar os pacotes Python utilizados no lado servidor da aplicação.

No mesmo diretório **server**, crie o arquivo **.env** e adicione o seguinte conteúdo:

```bash
PORTA=3000
DEBUG=False
```

Para rodar a aplicação em modo desenvolvimento, utilize o valor de "DEBUG" igual a "True" e para o modo produção use "False".

### Durante o Desenvolvimento

Ao desenvolver a aplicação digite o comando

`npm start`

no diretório **client** e digite o comando

`py src\app.py`

no diretório **server**. Utilize a aplicação acessando `http://127.0.0.1:3000`

### Em Produção

Para utilizar a aplicação em produção, digite o comando

`npm run build`

no diretório **client**.

Em seguida, para colocar a aplicação no ar, entre no diretório **server** e digite

`py src\app.py`
