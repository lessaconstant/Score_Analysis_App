import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import Home from './pages/Home'; // Página inicial
import Login from './pages/Login';
import UsersList from './pages/UsersList'; // Página de listagem de usuários
import Requests from './pages/Requests'; // Página de solicitações pendentes
import CreditRequest from './pages/CreditRequest'; // Página de solicitação de crédito
import Header from './components/Header'; // Componente Header
import Footer from './components/Footer'; // Componente Footer
import './App.css'; // Importa os estilos globais


const App: React.FC = () => {
  return (
    <Router>
      <Header /> {}
      
      <main>
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/login" element={<Login />} />
            <Route path="/users" element={<UsersList />} />
            <Route path="/requests" element={<Requests />} />
            <Route path="/credit-request" element={<CreditRequest />} />
        </Routes>
      </main>
      
      <Footer /> {}
    </Router>
  );
};

export default App;
