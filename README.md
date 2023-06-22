# Projeto de Banco de Dados - Loja Virtual da Charnelle

## Descrição
Este projeto tem como objetivo criar um sistema de cadastro para a loja virtual da Charnelle. O sistema permite o gerenciamento de produtos, clientes e pedidos.

## Tecnologias Utilizadas
- Python
- MySQL Workbench

## Estrutura do Banco de Dados

### Tabelas

#### Tabela "Produtos"
- `id_produto`: Identificador único do produto (chave primária)
- `nome`: Nome do produto
- `preco`: Preço do produto
- `descricao`: Descrição do produto

#### Tabela "Clientes"
- `id_cliente`: Identificador único do cliente (chave primária)
- `nome`: Nome do cliente
- `email`: Endereço de e-mail do cliente
- `telefone`: Número de telefone do cliente

#### Tabela "Pedidos"
- `id_pedido`: Identificador único do pedido (chave primária)
- `id_cliente`: Identificador do cliente (chave estrangeira referenciando a tabela "Clientes")
- `id_produto`: Identificador do produto (chave estrangeira referenciando a tabela "Produtos")
- `quantidade`: Quantidade do produto no pedido
- `data_pedido`: Data em que o pedido foi realizado

## Código em Python

Aqui está um exemplo de código Python que demonstra a integração com o banco de dados utilizando a biblioteca `mysql-connector-python`:

```python
import mysql.connector

# Conectando ao banco de dados
conn = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="nome_do_banco"
)

# Criando um cursor
cursor = conn.cursor()

# Exemplo de consulta
cursor.execute("SELECT * FROM Produtos")
produtos = cursor.fetchall()

for produto in produtos:
    print(produto)

# Fechando a conexão
conn.close()


