import React from 'react';
import { Container, Row, Col } from 'react-bootstrap';
import './Footer.css'; 

const Footer: React.FC = () => {
  return (
    <footer className="footer bg-dark text-white">
      <Container>
        <Row>
          <Col className="text-center py-3">
            &copy; 2024 Sistema de Crédito. Todos os direitos reservados.
          </Col>
        </Row>
      </Container>
    </footer>
  );
};

export default Footer;
