# 8 - Apuração de Urna Eletrônica: Recebemos uma lista gigantesca embaralhada 
# contendo os IDs dos candidatos que receberam votos. O voto em branco é o ID 0. O 
# sistema não sabe previamente quais são os IDs válidos. 
# Retorno exigido: Uma estrutura em formato de lista de listas (ex: [[id, 
# total_votos], ...]) resumindo a eleição, o ID do candidato vencedor e a 
# porcentagem de votos em branco. 

def apurar_votos(lista):
    resultado = []
    vencedor = 0
    maior = 0
    brancos = 0

    for i in lista:
        if i not in [j[0] for j in resultado]:
            cont = lista.count(i)
            resultado.append([i, cont])
            if i == 0:
                brancos = cont
            if i != 0 and cont > maior:
                maior = cont
                vencedor = i

    porcentagem = (brancos / len(lista)) * 100
    return resultado, vencedor, porcentagem

def main():
    votos = [1, 2, 1, 3, 0, 2, 1, 0, 3, 1, 2, 0]

    resultado, vencedor, porcentagem = apurar_votos(votos)

    print("resultado da eleicao:", resultado)
    print("candidato vencedor:", vencedor)
    print(f"votos em branco: {porcentagem:.2f}%")

main()
