import React from "react";
import { useNavigate } from "react-router-dom";
import "./Home.css";

const Home: React.FC = () => {
  const navigate = useNavigate();

  return (
    <div className="home-container">
      <div className="home-text">
        <h2>Bem-vindo ao Sistema de Crédito</h2>
        <p>Gerencie solicitações de crédito de forma rápida e eficiente.</p>
        <p>Você é...</p>
        <div className="button-container">
          <button
            className="role-button"
            onClick={() => navigate("/credit-request?role=cliente")}
          >
            Cliente
          </button>
          <button
            className="role-button"
            onClick={() => navigate("/users?role=gerente")}
          >
            Gerente
          </button>
        </div>
      </div>
    </div>
  );
};

export default Home;
