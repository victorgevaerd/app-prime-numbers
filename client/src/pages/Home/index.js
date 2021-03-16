import React, {useState} from 'react';
import {AiOutlineCloseCircle} from 'react-icons/ai'

import api from '../../api'
import './styles.css';

import Card from '../../components/Card';
import FormGroup from '../../components/FormGroup';

const Home = () => {
  const [numberOne, setNumberOne] = useState('');
  const [numberTwo, setNumberTwo] = useState('');
  const [primeNumbers, setPrimeNumbers] = useState('');
  const [history, setHistory] = useState([]);
  const [resultVisible, setResultVisible] = useState(false);
  const [historyVisible, setHistoryVisible] = useState(false);

  const onSearchPrimeNumbers = async () => {
    const data = {
      number_one: numberOne,
      number_two: numberTwo,
    };
    if (!validate()) {
      return false;
    }
    const response = await api.post(`primos`, data);
    if (Array.isArray(response.data)) {
      const arrayToString = response.data.join(', ');
      setPrimeNumbers(arrayToString);
      setResultVisible(true)
    } else {
      alert(response.data.message);
    }
  }

  const onSearchHistory = async () => {
    const response = await api.get(`historico`);
    setHistory(response.data);
    setHistoryVisible(true);
  }

  const validate = () => {
    function isNumeric(value) {
      return /^\d+$/.test(value);
    }

    if (!isNumeric(numberOne) || !isNumeric(numberTwo)) {
      alert('Favor informar somente números');
      return false;
    }

    return true;
  }

  return (
    <div className="jumbotron container">
      <h1 className="display-3">Olá! Seja bem vindo!</h1>
      <p className="lead">
        Gostaria de saber quais são os números primos de um determinado intervalo?
      </p>
      <hr className="my-4" />

      <Card title="Informe o intervalo" isVisible={false}>
        <div className="row">
          <div className="col-md-5">
            <FormGroup htmlFor="inputN1" label="Primeiro Número:">
              <input 
              type="text"
              maxLength="6"
              className="form-control" 
              id="inputN1"
              value={numberOne}
              onChange={(e) => setNumberOne(e.target.value)}/>          
            </FormGroup>
          </div>

          <div className="col-md-5">
            <FormGroup htmlFor="inputN2" label="Segundo Número:">
              <input 
              type="text"
              maxLength="6"
              className="form-control" 
              id="inputN2"
              value={numberTwo}
              onChange={(e) => setNumberTwo(e.target.value)}/>
            </FormGroup>
          </div>

          <div className="col-md-2" >
            <input 
              className="btn btn-primary searchButton" 
              type="button"
              value="Consultar" 
              onClick={onSearchPrimeNumbers} />
          </div>
        </div>
      </Card>

      {
        resultVisible ? 
          <Card title="Resultado" onClick={() => setResultVisible(false)}>
            <div>{primeNumbers}</div>
          </Card>
        :
          <div />
      }

      <button
        onClick={onSearchHistory} 
        className="btn btn-link historyLink">
          Verificar histórico de números consultados.
      </button>

      {
        historyVisible ?
          <Card title="Histórico de consultas" onClick={() => setHistoryVisible(false)}>
            <div>
              {history.map((h, index) => {
                return(
                  <p className="lead" key={index}>
                    <strong>
                      {`Números: ${h.number_one} e ${h.number_two}`}
                    </strong>
                  </p>
                )
              })}
            </div>
          </Card>
        :
          <div />
      }

    </div>
    
  );
};

export default Home;