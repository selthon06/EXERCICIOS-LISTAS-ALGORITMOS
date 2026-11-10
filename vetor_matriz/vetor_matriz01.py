# 1 - Escreva um programa em Python que solicite ao usuário a quantidade N de números 
# inteiros que deseja cadastrar. Construa uma lista vazia e preencha-a dinamicamente em 
# tempo de execução utilizando o método append(). Em seguida, percorra a lista e exiba: 
# (a) o maior e o menor valor digitados; (b) a média aritmética dos elementos; e (c) a 
# quantidade de números pares
# ==========================================
# EXERCÍCIO 1 — CADASTRO DE NUMEROS
# ==========================================

def analisar_numeros(lista):
    soma = 0
    pares = 0
    maior = lista[0]
    menor = lista[0]

    for i in lista:
        soma = soma + i
        if i > maior:
            maior = i
        if i < menor:
            menor = i
        if i % 2 == 0:
            pares = pares + 1
    media = soma / len(lista)
    return maior, menor, media, pares

def main():
    lista = []
    n = int(input("quantos numeros deseja cadastrar? "))
    for i in range(n):
        num = int(input("digite um numero: "))
        lista.append(num)
    maior, menor, media, pares = analisar_numeros(lista)

    print("maior valor:", maior)
    print("menor valor:", menor)
    print("media:", media)
    print("quantidade de pares:", pares)

main()
