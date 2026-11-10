# 9 - Desenvolva um programa completo em Python nativo para controle de estoque de 
# uma empresa. Utilize duas listas paralelas: `produtos` (strings) e `quantidades` 
# (inteiros). Implemente um menu interativo dentro de um laço `while` com as opções: 1. 
# Cadastrar Produto; 2. Listar Estoque; 3. Atualizar Quantidade; 4. Excluir Produto; 5. 
# Sair. Garantir a integridade dos índices sincronizados entre as duas listas. 

def cadastrar(produtos, quantidades):
    nome = input("nome do produto: ")
    qtd = int(input("quantidade: "))

    produtos.append(nome)
    quantidades.append(qtd)

    print("produto cadastrado")

def listar(produtos, quantidades):
    for i in range(len(produtos)):
        print(produtos[i], "-", quantidades[i])

def atualizar(produtos, quantidades):
    nome = input("produto para atualizar: ")

    if nome in produtos:
        pos = produtos.index(nome)
        qtd = int(input("nova quantidade: "))
        quantidades[pos] = qtd
        print("quantidade atualizada")
    else:
        print("produto nao encontrado")

def excluir(produtos, quantidades):
    nome = input("produto para excluir: ")

    if nome in produtos:
        pos = produtos.index(nome)
        produtos.pop(pos)
        quantidades.pop(pos)
        print("produto excluido")
    else:
        print("produto nao encontrado")

def main():
    produtos = []
    quantidades = []

    while True:
        print("\n1 - cadastrar produto")
        print("2 - listar estoque")
        print("3 - atualizar quantidade")
        print("4 - excluir produto")
        print("5 - sair")

        opcao = input("escolha uma opcao: ")

        if opcao == "1":
            cadastrar(produtos, quantidades)
        elif opcao == "2":
            listar(produtos, quantidades)
        elif opcao == "3":
            atualizar(produtos, quantidades)
        elif opcao == "4":
            excluir(produtos, quantidades)
        elif opcao == "5":
            print("saindo do sistema...")
            break
        else:
            print("opcao invalida")

main()
