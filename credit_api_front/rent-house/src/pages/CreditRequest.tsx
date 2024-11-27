import React, { useState } from 'react';
import axios from 'axios';

const CreditRequest: React.FC = () => {
  const [amount, setAmount] = useState('');
  const [description, setDescription] = useState('');
  const [userId, setUserId] = useState('');
  const [message, setMessage] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://localhost:8000/credit-requests/', {
        user: userId,
        amount: parseFloat(amount),
        description,
      });

      setMessage('Solicitação enviada com sucesso!');
      setError(null);
      setAmount('');
      setDescription('');
      setUserId('');
    } catch (err: any) {
      setError(err.response?.data?.error || 'Erro ao enviar a solicitação.');
      setMessage(null);
    }
  };

  return (
    <div>
      <h2>Solicitação de Crédito</h2>
      <form onSubmit={handleSubmit}>
        {message && <div style={{ color: 'green' }}>{message}</div>}
        {error && <div style={{ color: 'red' }}>{error}</div>}

        <div className="form-group">
          <label htmlFor="userId">ID do Usuário</label>
          <input
            type="text"
            id="userId"
            value={userId}
            onChange={(e) => setUserId(e.target.value)}
            className="form-control"
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="amount">Valor Solicitado</label>
          <input
            type="number"
            id="amount"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            className="form-control"
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="description">Motivo</label>
          <textarea
            id="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            className="form-control"
            required
          ></textarea>
        </div>

        <button type="submit" className="btn btn-primary">Enviar Solicitação</button>
      </form>
    </div>
  );
};

export default CreditRequest;
