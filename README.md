# Cashback
Sistema de cashback para compra de revendedoras.


## Pré requisito

- Poetry [https://python-poetry.org/docs/#installation]


## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/anaplopes/cashback.git
```

Entre no diretório do projeto

```bash
  cd cashback
```

Instale as dependências

```bash
  make install
```

Inicie o servidor

```bash
  make start
```


## Rodando os testes

Para rodar os testes, rode o seguinte comando

```bash
  make test
```


## Documentação da API

#### Retorna todos os itens

```http
  GET /api/items
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `api_key` | `string` | **Obrigatório**. A chave da sua API |

#### Retorna um item

```http
  GET /api/items/${id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. O ID do item que você quer |

#### add(num1, num2)

Recebe dois números e retorna a sua soma.

