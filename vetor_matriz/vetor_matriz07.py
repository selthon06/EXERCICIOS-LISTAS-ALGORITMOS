# 7 - Dada a matriz nativa 3x2 `matriz = [[1, 2], [3, 4], [5, 6]]`: (a) Permita que o usuário 
# atualize o valor da linha 1, coluna 0 para 99; (b) Escreva uma função que construa e 
# retorne a matriz transposta (tamanho 2x3), onde as linhas da matriz original viram 
# colunas. 

def transpor_matriz(matriz):
    nova = []
    for j in range(2):
        linha = []

        for i in range(3):
            linha.append(matriz[i][j])
        nova.append(linha)

    return nova

def main():
    matriz = [[1, 2], [3, 4], [5, 6]]
    matriz[1][0] = 99
    print("matriz atualizada:", matriz)
    resultado = transpor_matriz(matriz)
    print("matriz transposta:")

    for i in resultado:
        print(i)

main()
