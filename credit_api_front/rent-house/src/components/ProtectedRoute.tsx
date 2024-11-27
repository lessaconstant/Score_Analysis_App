import React from 'react';
import { useNavigate } from 'react-router-dom';

interface ProtectedRouteProps {
  isManager: boolean;
  children: React.ReactNode;
  redirectPath: string;
}

const ProtectedRoute: React.FC<ProtectedRouteProps> = ({
  isManager,
  children,
  redirectPath,
}) => {
  const navigate = useNavigate();

  if (!isManager) {
    // Redireciona para a página de login ou página de erro
    navigate(redirectPath);
    return null; // Não renderiza a rota protegida
  }

  return <>{children}</>;
};

export default ProtectedRoute;
