# Cashback
Sistema de cashback para compra de revendedoras.


## Documentação da API

```http
  GET /docs
```

```http
  GET /redoc
```


## Pré requisito

- [Pyenv](https://realpython.com/intro-to-pyenv/#installing-pyenv)
- [Poetry](https://python-poetry.org/docs/#installation)
- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

- Instalar pacotes essenciais (Ubuntu/Debian)
  ```bash
    sudo apt-get update && apt-get install -y make curl build-essential
  ```


## Rodando em ambiente de desenvolvimento

Clone o projeto

```bash
  git clone https://github.com/anaplopes/cashback.git
```

Entre no diretório do projeto

```bash
  cd cashback
```

Preparando o ambiente

```bash
  make prepare
```

Instale as dependências

```bash
  make install
```

Adicione as variaveis de ambiente no arquivo `.env.dev`
  - DB_URI: "postgresql://{DB_USER}:{DB_PASSWORD}@localhost:5432/{DB_NAME}"
  - GB_API_URL: url da API Grupo Boticario
  - GB_TOKEN: token da API Grupo Boticario

Inicie o container do banco de dados

```bash
  make up-db
```

Inicie o servidor

```bash
  make runserver
```

Para rodar os testes, rode o seguinte comando

```bash
  make test
```


## Rodando no docker

Adicione as variaveis de ambiente no arquivo `.env`

  - Obrigatório
    - DB_URI="postgresql://{DB_USER}:{DB_PASSWORD}@db:5432/{DB_NAME}"
    - GB_API_URL: url da API Grupo Boticario
    - GB_TOKEN: token da API Grupo Boticario

  - Opcional (***Essa mudança afetará a configuração DB_URI nos arquivos `.env*`)
    - DB_USER: usuario do banco de dados
    - DB_PASSWORD: senha do banco de dados
    - DB_NAME: nome do banco de dados

Inicie todos os containers

```bash
  make up
```

Parar os containers

```bash
  make down
```

Limpar o docker

```bash
  make clean
```
