# Biblioteca API

Este é um projeto de API para gerenciar uma biblioteca, desenvolvido com Django e Django REST Framework.

## Funcionalidades

- Adicionar, listar, atualizar e deletar livros.
- Cada livro possui os seguintes campos:
  - Título
  - Autor
  - Ano de Leitura
  - Nota
  - Comentário
- Autenticação JWT para proteger os endpoints da API.

## Tecnologias Utilizadas

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Django REST Framework SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

## Requisitos

- Python 3.8+
- Django 3.2+
- Django REST Framework 3.12+
- Django REST Framework SimpleJWT

## Instalação

1. Clone o repositório:

   ```sh
   git clone https://github.com/seu-usuario/biblioteca-api.git
   cd biblioteca-api
   ```

2. Crie um ambiente virtual e ative-o:

   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências:

   ```sh
   pip install -r requirements.txt
   ```

4. Crie um arquivo [.env](http://_vscodecontentref_/1) na raiz do projeto e adicione suas variáveis de ambiente:

   ```env
   SECRET_KEY=sua_chave_secreta
   DEBUG=True
   ENGINE=django.db.backends.postgresql
   DB_NAME=nome_do_banco
   DB_USER=usuario_do_banco
   DB_PASSWORD=senha_do_banco
   DB_HOST=localhost
   DB_PORT=5432
   ```

5. Aplique as migrações:

   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Crie um superusuário para acessar o admin do Django:

   ```sh
   python manage.py createsuperuser
   ```

7. Inicie o servidor de desenvolvimento:

   ```sh
   python manage.py runserver
   ```

8. Acesse a API em `http://127.0.0.1:8000/api/books/`.

## Endpoints

- `POST /api/token/` - Obter token JWT.
- `POST /api/token/refresh/` - Atualizar token JWT.
- `GET /api/books/` - Lista todos os livros (requer autenticação).
- `POST /api/books/` - Adiciona um novo livro (requer autenticação).
- `GET /api/books/{id}/` - Detalha um livro específico (requer autenticação).
- `PUT /api/books/{id}/` - Atualiza um livro específico (requer autenticação).
- `DELETE /api/books/{id}/` - Deleta um livro específico (requer autenticação).

## Exemplo de Requisição HTTP

### Obter token JWT

```http
POST http://127.0.0.1:8000/api/token/
Content-Type: application/json

{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```
