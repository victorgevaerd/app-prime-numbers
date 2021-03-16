import axios from 'axios';

const URL_BASE = 'http://127.0.0.1:5000/api/'

const api = axios.create({
  baseURL: URL_BASE
});

export default api;