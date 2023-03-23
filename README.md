# Cashback
Sistema de cashback para compra de revendedoras.


## Pré requisito

- Intalar o [Pyenv](https://realpython.com/intro-to-pyenv/#installing-pyenv)
- Instalar o [Poetry](https://python-poetry.org/docs/#installation)


## Rodando localmente

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

Inicie o container db

```bash
  make up-db
```

Instale as dependências

```bash
  make install
```

Inicie o servidor

```bash
  make runserver
```


## Rodando os testes

Para rodar os testes, rode o seguinte comando

```bash
  make test
```


## Documentação da API

```http
  GET /docs
```


## Rodando no docker

Inicie os containers

```bash
  make up
```

Parar os containers

```bash
  make down
```
