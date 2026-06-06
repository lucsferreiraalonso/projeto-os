import { useEffect, useState } from 'react'
import api from './services/api'
import ClienteForm from './components/ClienteForm';

function App() {
  return (
    <div style={{ padding: '40px', fontFamily: 'sans-serif' }}>
      <h1>Sistema de OS</h1>
      <ClienteForm />
    </div>
  );
}

export default App;

/*
function App() {
  const [mensagem, setMensagem] = useState('Conectando ao servidor...')

  // Assim que a tela carregar, o React vai buscar os dados no Python
  useEffect(() => {
    api.get('/')
      .then(response => {
        setMensagem(response.data.mensagem)
      })
      .catch(error => {
        setMensagem('Erro ao conectar com o servidor Python.')
        console.error(error)
      })
  }, [])

  return (
    <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
      <h1>Sistema de Ordem de Serviço</h1>
      <p><strong>Status do Backend:</strong> {mensagem}</p>
    </div>
  )
}

export default App
*/