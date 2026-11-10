# 1 - Média Móvel: Escreva uma função que receba uma lista de números e um número 
# inteiro k (tamanho da janela). A função deve retornar uma lista com as médias de cada 
# sublista contígua de tamanho k.

def media_movel(lista, k):
    medias = []

    for i in range(len(lista) - k + 1):
        soma = 0
        for j in range(i, i + k):
            soma = soma + lista[j]
        media = soma / k
        medias.append(media)

    return medias

def main():
    lista = [2, 4, 6, 8, 10]
    k = 3
    resultado = media_movel(lista, k)

    print("medias:", resultado)

main()
