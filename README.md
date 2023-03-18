# Cashback
Sistema de cashback para compra de revendedoras.


## Pré requisito

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

#### Validar funcionamento da API

```http
  GET /api/v1/cashback/health
```


#### Validar um login

```http
  POST /api/v1/cashback/auth
```

| Parâmetro   | Tipo       | Descrição                            |
| :---------- | :--------- | :----------------------------------- |
| `email`     | `string`   | **Obrigatório**. Email do revendedor |
| `password`  | `string`   | **Obrigatório**. Senha do revendedor |


#### Cadastra um novo revendedor

```http
  POST /api/v1/cashback/register/dealer
```

| Parâmetro   | Tipo       | Descrição                            |
| :---------- | :--------- | :----------------------------------- |
| `name`      | `string`   | **Obrigatório**. Nome do revendedor  |
| `cpf`       | `string`   | **Obrigatório**. CPF do revendedor   |
| `email`     | `string`   | **Obrigatório**. Email do revendedor |
| `password`  | `string`   | **Obrigatório**. Senha do revendedor |


#### Cadastra nova compra

```http
  POST /api/v1/cashback/register/purchase
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `code`      | `string`   | **Obrigatório**. Código da compra   |
| `date`      | `string`   | **Obrigatório**. Data da compra     |
| `value`     | `float`    | **Obrigatório**. Valor da compra    |
| `cpf`       | `string`   | **Obrigatório**. CPF do revendedor  |


#### Retorna compras cadastradas

```http
  GET /api/v1/cashback/list/purchases/${cpf}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `cpf`       | `string`   | **Obrigatório**. CPF do revendedor          |


#### Retorna acumulado de cashback

```http
  GET /api/v1/cashback/full/${cpf}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `cpf`       | `string`   | **Obrigatório**. CPF do revendedor          |
