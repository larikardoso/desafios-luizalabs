# 🏦 API Bancária Assíncrona — FastAPI

Este projeto é uma **API bancária assíncrona** desenvolvida em **FastAPI**, que permite o gerenciamento de **contas correntes, depósitos, saques e extrato**, utilizando **autenticação JWT** para garantir segurança e controle de acesso.

O objetivo do projeto é simular um sistema bancário simples, aplicando boas práticas de desenvolvimento backend, modelagem de dados e segurança.

---

## 🚀 Funcionalidades

A API oferece os seguintes recursos:

### 🔐 Autenticação
- Cadastro de usuários  
- Login com geração de **JWT (JSON Web Token)**  
- Proteção de endpoints com autenticação  

### 💳 Contas Correntes
- Criação de conta bancária vinculada ao usuário autenticado  
- Cada usuário pode possuir uma ou mais contas  

### 💰 Transações
- **Depósito em conta**  
- **Saque em conta**  
- Validação de saldo disponível  
- Bloqueio de valores negativos  

### 📄 Extrato
- Listagem de todas as transações de uma conta  
- Exibição de:
  - Tipo da operação (depósito ou saque)  
  - Valor  
  - Data e hora  
  - Saldo após a transação  

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11+**
- **FastAPI**
- **SQLAlchemy (modo assíncrono)**
- **PostgreSQL**
- **JWT (python-jose)**
- **Pydantic**
- **Alembic (migrations)**
- **Docker (opcional)**

---

## 🧠 Regras de Negócio Implementadas

- ❌ Não é permitido depositar valores negativos  
- ❌ Não é permitido sacar valores negativos  
- ❌ Não é permitido sacar mais do que o saldo disponível  
- 🔐 Apenas usuários autenticados podem movimentar suas contas  
- 🔗 Cada transação é vinculada a uma conta específica  

---

## 📌 Principais Endpoints

| Método | Rota | Descrição |
|------|------|---------|
| POST | `/auth/register` | Cadastro de usuário |
| POST | `/auth/login` | Login e geração do JWT |
| POST | `/accounts` | Criar conta corrente |
| POST | `/transactions/deposit` | Realizar depósito |
| POST | `/transactions/withdraw` | Realizar saque |
| GET | `/accounts/{account_id}/statement` | Consultar extrato |

---

## 📑 Documentação

A API conta com documentação automática via OpenAPI (Swagger):

📍 Acesse em:  
`http://localhost:8000/docs`

---
