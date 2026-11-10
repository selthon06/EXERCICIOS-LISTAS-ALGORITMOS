# 2 - Dada a lista estática de salários `salarios = [2500.0, 3200.0, 1800.0, 4500.0, 
# 2100.0]`: (a) Atualize o salário no índice 2 para 2300.0; (b) Peça ao usuário um valor de 
# salário para buscar e verificar se existe na lista usando o operador `in`; (c) Se existir, 
# remova-o usando `.remove()`; (d) Extraia e remova o último elemento da lista utilizando 
# `.pop()` e exiba o elemento removido. 

def alterar_salarios(salarios):
    salarios[2] = 2300.0
    valor = float(input("digite o salario para buscar: "))
    if valor in salarios:
        salarios.remove(valor)
        print("salario removido")
    else:
        print("salario nao encontrado")
    removido = salarios.pop()
    print("elemento removido pelo pop:", removido)
    return salarios

def main():
    salarios = [2500.0, 3200.0, 1800.0, 4500.0, 2100.0]
    salarios = alterar_salarios(salarios)
    print("lista atualizada:", salarios)

main()
