# 6 - Construa um programa em Python nativo para ler uma matriz 3x3 de inteiros 
# digitados pelo usuário: (a) Preencha a matriz utilizando laços aninhados em listas de 
# listas (`list[list]`); (b) Imprima a matriz em formato tabular formatado; (c) Exiba os 
# elementos da diagonal principal (onde índice da linha i == coluna j) e da diagonal 
# secundária (onde i + j == 2). 
import numpy as np

def alterar_notas(notas):
    notas = np.insert(notas, 2, 7.0)
    notas[notas < 6.0] = 6.0
    notas = np.delete(notas, 4)
    return notas

def main():
    notas = np.array([5.5, 8.0, 4.5, 9.0, 6.5])
    resultado = alterar_notas(notas)
    print("notas atualizadas:", resultado)
main()
