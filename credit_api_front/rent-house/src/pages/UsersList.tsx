import React, { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import "./UsersList.css";

const UsersList: React.FC = () => {
  const [users, setUsers] = useState<any[]>([]);
  const [selectedUser, setSelectedUser] = useState<any | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const location = useLocation();
  const navigate = useNavigate();

  
  useEffect(() => {
    const role = new URLSearchParams(location.search).get("role");
    if (role !== "gerente") {
      navigate("/"); 
    }
  }, [location, navigate]);

  // Fetch de usuários
  useEffect(() => {
    fetch("http://localhost:8000/api/users/")
      .then((res) => res.json())
      .then((data) => {
        console.log("Dados recebidos da API:", data);
        setUsers(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Erro na requisição:", error);
        setLoading(false);
      });
  }, []);

  return (
    <div className="users-container">
      <h1>Lista de Clientes</h1>

      {loading ? (
        <div className="loading">Carregando...</div>
      ) : (
        <table className="users-table">
          <thead>
            <tr>
              <th>Nome</th>
              <th>E-mail</th>
              <th>Limite de Crédito</th>
              <th>Ações</th>
            </tr>
          </thead>
          <tbody>
            {users.map((user) => (
              <tr key={user.id}>
                <td>{user.username}</td>
                <td>{user.email}</td>
                <td>R$ {user.credit_limit}</td>
                <td>
                  <button
                    className="view-more-btn"
                    onClick={() => setSelectedUser(user)}
                  >
                    Ver mais
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}

      {selectedUser && (
        <div className="user-modal">
          <div className="modal-content">
            <h2>Detalhes do Cliente</h2>
            <p><strong>Nome:</strong> {selectedUser.username}</p>
            <p><strong>E-mail:</strong> {selectedUser.email}</p>
            <p><strong>Limite de Crédito:</strong> R$ {selectedUser.credit_limit}</p>
            <p><strong>Score de Crédito Mais Recente:</strong> {selectedUser.credit_score}</p>
            <p><strong>Meses Inativos:</strong> {selectedUser.inactive_months_12m}</p>
            <hr />
            <p><strong>Nos Últimos 12 Meses</strong></p>
            <p><strong>Interações:</strong> {selectedUser.interactions_12m}</p>
            <p><strong>Compras Realizadas:</strong> {selectedUser.products_purchased_12m}</p>
            <p><strong>Transações:</strong> {selectedUser.transaction_count_12m}</p>
            <p><strong>Valor Total das Transações:</strong> R$ {selectedUser.transaction_value_12m}</p>
            <button
              className="close-btn"
              onClick={() => setSelectedUser(null)}
            >
              Fechar
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default UsersList;
