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

## Tecnologias Utilizadas

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)

## Requisitos

- Python 3.8+
- Django 3.2+
- Django REST Framework 3.12+

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

4. Crie um arquivo [.env](http://_vscodecontentref_/0) na raiz do projeto e adicione suas variáveis de ambiente:

    ```env
    SECRET_KEY=sua_chave_secreta
    DEBUG=True
    ```

5. pliqueA as migrações:

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Inicie o servidor de desenvolvimento:

    ```sh
    python manage.py runserver
    ```

7. Acesse a API em `http://127.0.0.1:8000/api/books/`.

## Endpoints

- `GET /api/books/` - Lista todos os livros.
- `POST /api/books/` - Adiciona um novo livro.
- `GET /api/books/{id}/` - Detalha um livro específico.
- `PUT /api/books/{id}/` - Atualiza um livro específico.
- `DELETE /api/books/{id}/` - Deleta um livro específico.

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Faça push para a branch (`git push origin feature/nova-feature`).
5. Crie um novo Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
