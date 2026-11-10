# 2 - Deslocamento (Shift) à Direita: Crie uma função que receba uma lista e um inteiro n. 
# A função deve retornar uma nova lista com os elementos deslocados n posições para a 
# direita. Os elementos que "saírem" do final devem reaparecer no início. 

def deslocar(lista, n):
    n = n % len(lista)
    nova = lista[-n:] + lista[:-n]

    return nova

def main():
    lista = [1, 2, 3, 4, 5]
    n = 2
    resultado = deslocar(lista, n)

    print("lista original:", lista)
    print("lista deslocada:", resultado)

main()
