# 3 - Crie um vetor com 10 números inteiros de 1 a 10. Utilizando a técnica de fatiamento 
# (slicing) do Python: (a) Gere uma sublista contendo apenas os elementos localizados 
# nos índices pares; (b) Gere uma sublista contendo apenas os números ímpares (por 
# valor); (c) Crie uma cópia da lista inteira invertida sem utilizar o método `.reverse()`. 

def analisar_lista(lista):
    indices = lista[::2]
    impares = [i for i in lista if i % 2 != 0]
    invertida = lista[::-1]
    return indices, impares, invertida

def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    indices, impares, invertida = analisar_lista(lista)

    print("elementos dos indices pares:", indices)
    print("numeros impares:", impares)
    print("lista invertida:", invertida)

main()
