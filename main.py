import mysql.connector
from getpass import getpass

# Função para conectar ao banco de dados
def conectar_bd():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root2",
        password="Cassandra",
        database="charnelle"
    )
    return conexao

# Função para exibir o menu do usuario
def usuarios_menu():
    print("===== MENU =====")
    print("1. Cadastrar usuario")
    print("2. Alterar a senha")
    print("3. Login")
    print("4. Sair")

# Função para exibir o menu contendo os itens
def exibir_menu():
    print("===== MENU =====")
    print("1. Inserir item")
    print("2. Consultar item")
    print("3. Alterar item")
    print("4. Remover item")
    print("5. Inventario")
    print("6. Sair")

# Função para o usuario fazer o login
def login_usuario():
    conexao = conectar_bd()
    cursor = conexao.cursor()
    nome = input("Digite o nome do usuário: ")
    senha = getpass("Digite a senha: ")
    query = "SELECT * FROM usuarios WHERE nome = %s and senha = %s"
    valores = (nome,senha)
    cursor.execute(query, valores)
    login = cursor.fetchone()
    if login is not None:
        print("OLá, seja bem-vindo(a)!")

    else:
        print("Login ou senha incorreta, por favor tente novamente.")

    cursor.close()
    conexao.close()
    return login

#Função para inserir um item na tabela de itens
def inserir_item():
    conexao = conectar_bd()
    cursor = conexao.cursor()

    nome = input("Digite o nome do item: ")
    descricao = input("Digite a descrição do item: ")
    preco = float(input("Digite o preço do item: "))

    if preco > 200:
        desconto = preco * 0.1  # Aplicar um desconto de 10%
        preco_com_desconto = preco - desconto
        mensagem_desconto = f"Desconto aplicado! Valor com desconto: R$ {preco_com_desconto:.2f}"
    else:
        mensagem_desconto = "Valor do item não atende aos critérios para aplicar desconto."

    # Mostra a mensagem de desconto
    print(mensagem_desconto)

    # Insere os dados no banco de dados
    query = "INSERT INTO itens (nome, descricao, preco) VALUES (%s, %s, %s)"
    valores = (nome, descricao, preco)

    cursor.execute(query, valores)
    conexao.commit()

    print("Item inserido com sucesso!")

    cursor.close()
    conexao.close()

# Função para consultar um item na tabela de itens
def consultar_item():
    conexao = conectar_bd()
    cursor = conexao.cursor()

    id = int(input("Digite o codigo a ser consultado: "))

    # Consulta o item no banco de dados
    query = "SELECT * FROM itens WHERE id = %s"
    valores = (id,)

    cursor.execute(query, valores)
    item = cursor.fetchone()

    if item is not None:
        print("Id:", item[0])
        print("Nome:", item[1])
        print("Descrição:", item[2])
        print("Preço:", item[3])
    else:
        print("Item não encontrado.")

    cursor.close()
    conexao.close()

# Função para alterar um item na tabela de itens
def alterar_item():
    conexao = conectar_bd()
    cursor = conexao.cursor()

    id_item = int(input("Digite o ID do item a ser alterado: "))

    nome = input("Digite o novo nome do item: ")
    descricao = input("Digite a nova descrição do item: ")
    preco = float(input("Digite o novo preço do item: "))

    # Atualiza os dados no banco de dados
    query = "UPDATE itens SET nome = %s, descricao = %s, preco = %s WHERE id = %s"
    valores = (nome, descricao, preco, id_item)

    cursor.execute(query, valores)
    conexao.commit()

    if cursor.rowcount > 0:
        print("Item alterado com sucesso!")
    else:
        print("Falha ao alterar o item.")

    cursor.close()
    conexao.close()

# Função para remover um item na tabela de itens
def remover_item():
    conexao = conectar_bd()
    cursor = conexao.cursor()

    id_item = int(input("Digite o ID do item a ser removido: "))

    # Remove o item do banco de dados
    query = "DELETE FROM itens WHERE id = %s"
    valores = (id_item,)

    cursor.execute(query, valores)
    conexao.commit()

    if cursor.rowcount > 0:
        print("Item removido com sucesso!")
    else:
        print("Falha ao remover o item.")

    cursor.close()
    conexao.close()

# Função para consultar o inventário
def consultar_inventario():
    conexao = conectar_bd()
    cursor = conexao.cursor()

    query = "SELECT * FROM itens"
    cursor.execute(query)

    # Recuperar os resultados da consulta
    resultados = cursor.fetchall()

    # Exibir os resultados na forma de inventário
    print("Inventário:")
    for item in resultados:
        codigo= item[0]
        nome = item[1]
        descricao = item[2]
        preco = item[3]
        print(f"Id: {codigo}, Nome: {nome}, Descrição: {descricao}, Preço: {preco}")

    cursor.close()
    conexao.close()


# Função para cadastrar um novo usuário no sistema
def cadastrar_usuario():
    conexao = conectar_bd()
    cursor = conexao.cursor()

    nome = input("Digite o nome do usuário: ")
    senha = input("Digite a senha: ")
    if len(senha) <5:
        print("Sua senha é curta demais para ser aceita, por favor insira a partir de 5 caracteres")
    else:# Insere os dados do usuário no banco de dados
        query = "INSERT INTO usuarios (nome, senha) VALUES (%s, %s)"
        valores = (nome, senha)

        cursor.execute(query, valores)
        conexao.commit()

        print("Usuário cadastrado com sucesso!")

        cursor.close()
        conexao.close()


# Função para alterar a senha de um usuário
def alterar_senha():
    conexao = conectar_bd()
    cursor = conexao.cursor()

    nome = input("Digite o nome do usuário: ")
    nova_senha = input("Digite a nova senha: ")

    # Atualiza a senha do usuário no banco de dados
    query = "UPDATE usuarios SET senha = %s WHERE nome = %s"
    valores = (nova_senha, nome)

    cursor.execute(query, valores)
    conexao.commit()

    if cursor.rowcount > 0:
        print("Senha alterada com sucesso!")
    else:
        print("Falha ao alterar a senha.")

    cursor.close()
    conexao.close()

# Função principal para executar o menu no usuario e dos itens

def main():
    executar = True
    checkin = True

    while checkin:
        usuarios_menu()
        opcao1=int(input("Escolha uma opção: "))

        if opcao1 == 1:
            cadastrar_usuario()
        elif opcao1 == 2:
            alterar_senha()
        elif opcao1 == 3:
            login = login_usuario()
            logado = login is not None
            if logado:
                checkin = False


        elif opcao1 == 4:
            executar = False

            checkin = False


    while executar:
        exibir_menu()
        opcao2 = int(input("Escolha uma opção: "))

        if opcao2 == 1:
            inserir_item()
        elif opcao2 == 2:
            consultar_item()
        elif opcao2 == 3:
            alterar_item()
        elif opcao2 == 4:
            remover_item()
        elif opcao2 == 5:
            consultar_inventario()
        elif opcao2 == 6:
            executar = False
        else:
            print("Opção inválida. Tente novamente!")
        #input("Aperte enter para voltar ao menu")


    print("Até breve!")

if __name__ == "__main__":
    main()

