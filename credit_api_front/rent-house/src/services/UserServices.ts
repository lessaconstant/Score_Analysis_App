import {api} from  '../axiosconfig';

export interface User {
    id: number;
    username: string; 
    email: string;    
    age: number;
    gender: string;
    dependents: number;
    education_level: string;
    annual_income: number;
    card_type: string;
    products_purchased_12m: number;
    interactions_12m: number;
    inactive_months_12m: number;
    credit_limit: number;
    transaction_value_12m: number;
    transaction_count_12m: number;
    credit_score: number;
  }

  export const UserService = {
    // Método para listar usuários
    listUsers: async () => {
      try {
        const response = await api.get<User[]>("/users/");
        return response;
      } catch (error) {
        console.error("Erro ao buscar usuários:", error);
        throw error;
      }
    }}
