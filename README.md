
# API de Gerenciamento de Usuários e Profissionais

Este projeto é uma API desenvolvida em Django e Django Rest Framework (DRF) para gerenciamento de usuários e profissionais de saúde. A API permite registrar usuários, fazer login, listar e gerenciar profissionais, e outras operações relacionadas.

## Tecnologias Utilizadas

- Django
- Django Rest Framework
- Django Rest Framework SimpleJWT
- PostgreSQL (ou outro banco de dados)

## Instalação

### Pré-requisitos

Certifique-se de ter Python e pip instalados em seu ambiente.

### Passos para Configuração

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu_usuario/seu_repositorio.git
   cd seu_repositorio
   ```

2. **Crie um ambiente virtual e ative-o:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux ou Mac
   venv\Scripts\activate  # Para Windows
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados no arquivo `settings.py`:**

   Altere as configurações do banco de dados conforme necessário.

5. **Faça as migrações:**

   ```bash
   python manage.py migrate
   ```

6. **Crie um superusuário (opcional):**

   ```bash
   python manage.py createsuperuser
   ```

7. **Inicie o servidor:**

   ```bash
   python manage.py runserver
   ```

Agora, você pode acessar a API em `http://127.0.0.1:8000/api/`.


## Documentação da API

### Autenticação

- **Registrar Usuário**
  - **Endpoint:** `/api/auth/register/`
  - **Método:** `POST`
  - **Corpo da Requisição:**
    ```json
    {
      "username": "seu_usuario",
      "password": "sua_senha",
      "email": "seu_email@example.com"
    }
    ```

- **Login de Usuário**
  - **Endpoint:** `/api/auth/login/`
  - **Método:** `POST`
  - **Corpo da Requisição:**
    ```json
    {
      "username": "seu_usuario",
      "password": "sua_senha"
    }
    ```

- **Token de Atualização**
  - **Endpoint:** `/api/auth/token/refresh/`
  - **Método:** `POST`
  - **Corpo da Requisição:**
    ```json
    {
      "refresh": "token_refresh_aqui"
    }
    ```

### Usuários

- **Detalhes do Usuário Autenticado**
  - **Endpoint:** `/api/user/`
  - **Método:** `GET`
  - **Requer Autenticação**

- **Deletar Usuário Autenticado**
  - **Endpoint:** `/api/user/`
  - **Método:** `DELETE`
  - **Requer Autenticação**

- **Listar Todos os Usuários**
  - **Endpoint:** `/api/users/`
  - **Método:** `GET`
  - **Não requer autenticação**

### Profissionais

- **Listar Profissionais**
  - **Endpoint:** `/api/profissionais/`
  - **Método:** `GET`
  - **Requer Autenticação**

- **Criar Profissional**
  - **Endpoint:** `/api/profissionais/`
  - **Método:** `POST`
  - **Corpo da Requisição:**
    ```json
    {
      "nome": "Nome do Profissional",
      "especialidade": "Especialidade",
      "contato": "Contato"
    }
    ```

- **Detalhes de um Profissional**
  - **Endpoint:** `/api/profissionais/<int:id>/`
  - **Método:** `GET`
  - **Requer Autenticação**

- **Atualizar Profissional**
  - **Endpoint:** `/api/profissionais/<int:id>/`
  - **Método:** `PUT`
  - **Corpo da Requisição:**
    ```json
    {
      "nome": "Nome Atualizado",
      "especialidade": "Nova Especialidade",
      "contato": "Novo Contato"
    }
    ```

- **Deletar Profissional**
  - **Endpoint:** `/api/profissionais/<int:id>/`
  - **Método:** `DELETE`
  - **Requer Autenticação**

## Contribuição

Sinta-se à vontade para enviar pull requests ou relatar problemas.

## Licença

Este projeto é licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.
