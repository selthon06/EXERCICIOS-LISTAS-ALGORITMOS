# 3 - Concatenação Alternada: Desenvolva uma função que receba duas listas (de 
# tamanhos possivelmente diferentes) e retorne uma única lista intercalando os elementos 
# de ambas até o fim da menor, adicionando o restante da maior ao final. 


def concatenar(lista1, lista2):
    nova = []
    maior = max(len(lista1), len(lista2))
    for i in range(maior):
        if i < len(lista1):
            nova.append(lista1[i])
        if i < len(lista2):
            nova.append(lista2[i])

    return nova

def main():
    lista1 = [1, 3, 5, 7]
    lista2 = [2, 4, 6]
    resultado = concatenar(lista1, lista2)

    print("lista intercalada:", resultado)
main()
