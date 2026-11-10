# 4 - Merge de Listas Ordenadas: Desenvolva uma função que receba duas listas que já 
# estão ordenadas de forma crescente. A função deve retornar uma única lista contendo 
# todos os elementos de ambas, também ordenada. Não é permitido concatenar e aplicar 
# algoritmo de ordenação depois. 


def merge(lista1, lista2):
    nova = []
    i = 0
    j = 0

    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            nova.append(lista1[i])
            i = i + 1
        else:
            nova.append(lista2[j])
            j = j + 1

    while i < len(lista1):
        nova.append(lista1[i])
        i = i + 1

    while j < len(lista2):
        nova.append(lista2[j])
        j = j + 1

    return nova

def main():
    lista1 = [1, 3, 5, 7]
    lista2 = [2, 4, 6, 8]

    resultado = merge(lista1, lista2)

    print("lista ordenada:", resultado)

main()
