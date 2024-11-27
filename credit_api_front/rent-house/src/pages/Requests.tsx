import React, { useState, useEffect } from "react";
import "./Requests.css";
import "../App.css";

const Requests = () => {
  const [requests, setRequests] = useState<any[]>([]);
  const [selectedRequest, setSelectedRequest] = useState<any | null>(null);
  const [statusMessage, setStatusMessage] = useState<string | null>(null);

  // Fetch de solicitações pendentes
  useEffect(() => {
    fetch("http://localhost:8000/api/credit-analysis/pending/")
      .then((res) => res.json())
      .then((data) => {
        console.log("Dados recebidos:", data); // Verifique os campos aqui
        setRequests(data);
      })
      .catch((err) => console.error("Erro ao buscar solicitações:", err));
  }, []);

  // Atualiza o status da análise
  const handleStatusChange = (status: string) => {
    if (!selectedRequest) return;

    fetch(`http://localhost:8000/api/credit-analysis/${selectedRequest.user_id}/update/`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ status }),
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error("Erro ao atualizar status");
        }
        return res.json();
      })
      .then(() => {
        setStatusMessage(status === "A" ? "Crédito aceito" : "Crédito negado");
        setRequests((prev) =>
          prev.filter((request) => request.user_id !== selectedRequest.user_id)
        );
        setSelectedRequest(null);
      })
      .catch(() => {
        setStatusMessage("Erro ao atualizar status");
      });
  };

  return (
    <div className="requests-container">
      <h1>Solicitações de Crédito</h1>

      {statusMessage && <div className="status-message">{statusMessage}</div>}

      <table className="requests-table">
        <thead>
          <tr>
            <th>Nome</th>
            <th>Data</th>
            <th>Status</th>
            <th>Ações</th>
          </tr>
        </thead>
        <tbody>
          {requests.map((request) => (
            <tr key={request.user_id}>
              <td>{request.user_name}</td>
              <td>{request.analysis_date}</td>
              <td>{request.status}</td>
              <td>
                <button
                  className="review-btn"
                  onClick={() => setSelectedRequest(request)}
                >
                  Revisão
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {selectedRequest && (
        <div className="review-modal">
          <div className="modal-content">
            <h2>Revisão de Solicitação</h2>
            <p><strong>Nome:</strong> {selectedRequest.user_name}</p>
            <p><strong>Data:</strong> {selectedRequest.analysis_date}</p>
            <p><strong>Detalhes:</strong> {selectedRequest.detail}</p>
            <div className="modal-actions">
              <button
                className="approve-btn"
                onClick={() => handleStatusChange("A")}
              >
                Aprovar
              </button>
              <button
                className="reject-btn"
                onClick={() => handleStatusChange("R")}
              >
                Reprovar
              </button>
              <button
                className="close-btn"
                onClick={() => setSelectedRequest(null)}
              >
                Fechar
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Requests;
