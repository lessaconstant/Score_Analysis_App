
# Sistema de Análise de Crédito com API REST

  

Este projeto é um sistema de análise de crédito que utiliza uma API REST para integrar um modelo de Machine Learning (ML) com o objetivo de calcular o score de crédito dos clientes e determinar a elegibilidade para crédito. Desenvolvido como parte da avaliação para a matéria Laboratório de Programação 5, o foco é na criação e implementação de APIs REST.

  

## Funcionalidades

  

- Cadastro de Usuários

- Registro de Bancos

- Análise de Crédito com ML

- Registro de Transações

  

## Tecnologias Utilizadas

  

- Django e Django REST Framework

- Machine Learning (ML) para previsão de crédito

- SQLite/MySQL/PostgreSQL

- Pickle para carregar o modelo de ML

  

## Estrutura do Projeto

  

-  **users:** Gerencia os dados dos usuários.

-  **banks:** Armazena informações sobre os bancos.

-  **credit_analysis:** Realiza a análise de crédito e integra com o modelo de ML.

-  **transactions:** Registra as transações realizadas pelos usuários.

  

## Etapas de Desenvolvimento

  

O projeto será desenvolvido em três etapas, cada uma com suas próprias condições conforme a matéria pedir:

  

1.  **Primeira Etapa:**

- Implementação das APIs básicas para cadastro e gerenciamento de usuários.

- Criação de um modelo de dados para armazenar informações dos usuários, bancos e transações.

- Configuração inicial do sistema e integração básica das APIs.

  

- Necessário presença de :

	- 2 apps refentes ao tema

	- 5 modelos contendo relacionamentos ManytoMany e Foreign Key

	- Conter dados com os tipos CharField, IntegerField

	- Conter, no mínimo, 4 Serializers e 4 APIVIEW

	- Todos os modelos devem estar presentes no django admin

  

2.  **Segunda Etapa:**

- Descrição das condições e objetivos será fornecida posteriormente.

  

3.  **Terceira Etapa:**

- Descrição das condições e objetivos será fornecida posteriormente.

  

## Instruções de Teste

  

1. Clone o repositório e crie um ambiente virtual

```

git clone https://github.com/lessaconstant/score_analysis_api.git

cd score_analysis_api

python -m venv venv

source venv/bin/activate # No Windows use `venv\Scripts\activate`

```

  

2. Instale as dependências:

```

pip install -r requirements.txt

```

  

3. Configure o banco de dados e aplique as migrações:

```

python manage.py migrate

```

  

4. Adicione o arquivo model.pkl na raiz do projeto. Este arquivo será o algoritmo de machine learning que fará a análise de crédito. **Este arquivo é um modelo fictício (dummy)** e foi incluído apenas para o desenvolvimento e teste da API. Ele **não** é o modelo final treinado. O desenvolvimento e treinamento do algoritmo está sendo feito no notebook ML_Score.ipynb.

5. O dataset utilizado para a construção do modelo é fictício e pode ser encontrado neste link: [Análise de Crédito - Kaggle](https://www.kaggle.com/datasets/antonhyonhi/anlise-de-crdito-ebac).

  

6. Crie um superusuário para acessar o painel administrativo (opcional):

```

python manage.py createsuperuser

```

## Contribuições

Contribuições são bem-vindas. Envie um pull request ou abra uma issue para melhorias.