# 8 - Utilizando o NumPy: (a) Crie uma matriz 4x4 preenchida com números inteiros 
# aleatórios entre 10 e 99 (`np.random.randint()`); (b) Calcule a soma de cada linha 
# (axis=1) e a média de cada coluna (axis=0); (c) Altere a forma da matriz (reshape) de 
# 4x4 para 2x8 e exiba a nova estrutura.

import numpy as np

def analisar_matriz(matriz):
    soma = np.sum(matriz, axis=1)
    media = np.mean(matriz, axis=0)
    nova = matriz.reshape(2, 8)
  
    print("matriz original:")
    print(matriz)
    print("soma das linhas:", soma)
    print("media das colunas:", media)
    print("matriz 2x8:")
    print(nova)

def main():
    matriz = np.random.randint(10, 100, (4, 4))
    analisar_matriz(matriz)

main()
