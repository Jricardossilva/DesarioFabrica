# Fábrica de Software
## Desafio Back-End 2024.2 ##

** Desafio ** Um dos requisitos para ingressar na fábrica de software no periodo de 2024.2, foi resolver um desafio que consiste em criar uma aplicação de consumo de API com Python/Django.
A projeto deve possuir o CRUD com 2 ou mais classes, além de possuir capacidade de consumir uma API externa e guarda os dados em banco. Este projeto contém uma aplicação base para uma Editora desenvolvida em Django que implementa um CRUD (Create, Read, Update, Delete) usando Django REST Framework com duas entidades (Autor e Livro), além de consumir uma API externa para armazenar dados em um banco de dados local e externo (MySQL). Segue abaixo uma descrição das funcionalidades e tecnologias utilizadas neste desafio, bem como um passo-a-passo para execução do projeto.

## Funcionalidades

- **Gerenciamento de Livros**: Permite realizar todas as operações de CRUD de livros.
- **Gerenciamento de Autores**: Permite realizar todas as operações de CRUD de autores dos livros.

## Tecnologias Utilizadas

- **Backend**:
  - Python 3.12
  - Django 4.1
  - Django REST Framework
  - MySQL

## API's Disponíveis

  - GET /autor/ - Lista todos os autores
  - POST /autor/ - Salva um autor
  - GET /autor/{id}/ - Informações do autor especificado pelo id
  - PUT /autor/{id}/ - Atualiza um autor especificado pelo id
  - DELETE /autor/{id}/ - Deleta um autor especificado pelo id
  - GET /livros/ - Lista todos os livros
  - POST /livros/ - Salva um livro
  - GET /livros/{id}/ - Informações do livro especificado pelo id
  - PUT /livros/{id}/ - Atualiza um livro especificado pelo id
  - DELETE /livros/{id}/ - Deleta um livro especificado pelo id

## Execução do Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/Jricardossilva/DesarioFabrica.git
```

### 2. Criar o ambiente virtual

```bash
py -m venv venv
```

### 3. Ativar o ambiente virtual
- **Linux e Mac**:
```bash
source venv/bin/activate
```
- **Windows**:
```bash
venv\Scripts\activate
```

### 4. Instalação das dependências

```bash
pip install -r requirements.txt
```

### 5. Configuração do Banco de Dados

Edite o arquivo 'settings.py' para configurar o banco de dados. Substitua as informações do databases, conforme código abaixo.

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    
    #Banco de dados Externo
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'meu_banco',
        'USER': 'meu_usuario',
        'PASSWORD': 'minha_senha',
        'HOST': 'meu_host',
        'PORT': '3306'
   } ,
}
```

### 6. Migrar os modelos para o banco de dados

```bash
py manage.py makemigrations
py manage.py migrate
```

### 7. Executar o servidor

```bash
py manage.py runserver
```

### 8. Acessar a aplicação

- **Autor**:
```bash
http://localhost:8000/editora/autor/
```

- **Livros**:
```bash
http://localhost:8000/editora/livros/
```
