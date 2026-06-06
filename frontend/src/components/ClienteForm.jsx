import { useState } from 'react';
import api from '../services/api';

function ClienteForm() {
  const [formData, setFormData] = useState({ nome: '', email: '', telefone: '' });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.post('/clientes/', formData);
      alert('Cliente cadastrado com sucesso!');
      setFormData({ nome: '', email: '', telefone: '' }); // Limpa o formulário
    } catch (error) {
      alert('Erro ao cadastrar cliente.');
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '10px', maxWidth: '300px' }}>
      <h2>Novo Cliente</h2>
      <input type="text" placeholder="Nome" value={formData.nome} onChange={(e) => setFormData({...formData, nome: e.target.value})} required />
      <input type="email" placeholder="Email" value={formData.email} onChange={(e) => setFormData({...formData, email: e.target.value})} required />
      <input type="text" placeholder="Telefone" value={formData.telefone} onChange={(e) => setFormData({...formData, telefone: e.target.value})} required />
      <button type="submit">Cadastrar</button>
    </form>
  );
}

export default ClienteForm;