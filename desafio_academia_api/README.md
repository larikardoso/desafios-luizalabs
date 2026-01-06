# ⚡ Academia API

API REST desenvolvida com **FastAPI** para gerenciamento básico de uma academia.  
O projeto foi criado com foco em **boas práticas de backend**, organização de código e uso de padrões comuns em APIs modernas.

A aplicação permite o **cadastro e consulta de alunos**, utilizando um banco de dados relacional e validação de dados com Pydantic.

---

## 🧠 Sobre o projeto

Esta aplicação é uma **API backend**, ou seja:

- Não possui interface gráfica (frontend)
- Recebe requisições HTTP (`GET`, `POST`, etc.)
- Retorna respostas no formato **JSON**
- Utiliza **FastAPI**, que gera documentação automática

Para facilitar testes e validação dos endpoints, a API disponibiliza uma interface interativa via **Swagger UI**.

---

## 🧱 Tecnologias utilizadas

- Python 3
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- Uvicorn

---

## ▶️ Como rodar o projeto localmente

### 1️⃣ Criar e ativar o ambiente virtual

Depois de instalar as dependências, use o comando abaixo:

```bash
uvicorn main:app --reload
```

🔗 Acessos e testes

🌐 API (endereço base):
```bash
http://127.0.0.1:8000
```
📚 Swagger (onde você testa a API):
```
http://127.0.0.1:8000/docs
```
🧪 Exemplo de uso

Exemplo de cadastro de um aluno novo (JSON):
```json
{
  "nome": "Larissa Cardoso",
  "cpf": "012345678900",
  "idade": 30,
  "centro_treinamento": "FoxBox"
}
```


Se o CPF já existir, a API retorna:
```json
{
  "detail": "CPF já cadastrado"
}
```

🧰 Tecnologias usadas
- Python  
- FastAPI  
- SQLAlchemy  
- Pydantic  
- SQLite  
- FastAPI Pagination  
- Uvicorn

