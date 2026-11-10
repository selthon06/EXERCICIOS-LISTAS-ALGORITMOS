# 4 - Utilizando a biblioteca NumPy: (a) Crie um array 1D com os números inteiros de 10 
# a 50 (inclusive) com passo 5 usando `np.arange()`; (b) Eleve todos os elementos do 
# array ao quadrado de forma vetorizada (sem laço `for`); (c) Aplique uma filtragem por 
# indexação booleana para extrair apenas os valores superiores a 500. 

import numpy as np

def analisar_array():
    numeros = np.arange(10, 51, 5)
    quadrado = numeros ** 2
    maiores = quadrado[quadrado > 500]

    print("array original:", numeros)
    print("valores ao quadrado:", quadrado)
    print("valores maiores que 500:", maiores)

def main():
    analisar_array()
  
main()
