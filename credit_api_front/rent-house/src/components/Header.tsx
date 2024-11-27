import React from 'react';
import { Navbar, Button } from 'react-bootstrap';
import { useLocation, useNavigate, Link } from 'react-router-dom';
import './Header.css';

const Header: React.FC = () => {
  const location = useLocation();
  const navigate = useNavigate();

  const isUsersListPage = location.pathname === '/users';

  return (
    <Navbar bg="dark" variant="dark" className="header">
      {}
      <Link to="/" className="brand-center">
        <img
          src="../favicon_io/favicon.ico"
          alt="Ícone do Sistema de Crédito"
          width="30"
          height="30"
        />
        <span>NeoCred</span>
      </Link>

      {}
      {isUsersListPage && (
        <Button
          variant="outline-light"
          className="solicitations-button"
          onClick={() => navigate('/requests')}
        >
          🛎 Solicitações
        </Button>
      )}
    </Navbar>
  );
};

export default Header;
