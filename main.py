import mysql.connector
#testando dnv
#nao esta funcionando o git
# Função para conectar ao banco de dados
def conectar_bd():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="#C4n4d42k18",
        database="loja_roupas"
    )
    return conexao

# Função para exibir o menu
def exibir_menu():
    print("===== MENU =====")
    print("1. Inserir item")
    print("2. Consultar item")
    print("3. Alterar item")
    print("4. Remover item")
    print("5. Cadastrar usuário")
    print("6. Alterar senha")
    print("7. Sair")

# Função para inserir um item na tabela de itens
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

    # Imprima a mensagem de desconto
    print(mensagem_desconto)

    # Inserir os dados no banco de dados
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

    # Consultar o item no banco de dados
    query = "SELECT * FROM itens WHERE id = %s"
    valores = (id,)

    cursor.execute(query, valores)
    item = cursor.fetchone()

    if item is not None:
        print("ID:", item[0])
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

    # Atualizar os dados no banco de dados
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

    # Remover o item do banco de dados
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

# Função para cadastrar um novo usuário no sistema
def cadastrar_usuario():
    conexao = conectar_bd()
    cursor = conexao.cursor()

    nome = input("Digite o nome do usuário: ")
    senha = input("Digite a senha: ")

    # Inserir os dados do usuário no banco de dados
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

    # Atualizar a senha do usuário no banco de dados
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

# Função principal
def main():
    executar = True

    while executar:
        exibir_menu()
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            inserir_item()
        elif opcao == 2:
            consultar_item()
        elif opcao == 3:
            alterar_item()
        elif opcao == 4:
            remover_item()
        elif opcao == 5:
            cadastrar_usuario()
        elif opcao == 6:
            alterar_senha()
        elif opcao == 7:
            executar = False
        else:
            print("Opção inválida. Tente novamente.")

    print("Encerrando a aplicação...")

if __name__ == "__main__":
    main()

