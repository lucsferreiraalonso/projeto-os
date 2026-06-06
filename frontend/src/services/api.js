import axios from 'axios';

const api = axios.create({
  // Lembre-se de substituir pelo IP real da sua VM (ex: 192.168.1.50)
  baseURL: 'http://192.168.50.110:8000',
});

export default api;