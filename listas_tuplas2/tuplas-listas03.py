# 3 - O sistema do caixa gera um recibo na forma de uma lista de tuplas (codigo_produto, 
# quantidade, preco_unitario). 
# Você deve multiplicar valores internos da tupla para criar dados novos (valor total do 
# item), acumular um montante geral e guardar o registro do maior valor calculado. 
# Retorno Exigido: O valor total da compra e uma tupla (codigo_produto, 
# valor_total_do_item) representando exclusivamente o item que teve o maior custo 
# absoluto na nota fiscal. 
# Na Main: Monte uma lista de tuplas representando o "carrinho" de um cliente com 3 ou 
# mais itens diferentes. Execute a função recebendo os retornos e imprima no terminal o 
# valor total da nota fiscal (formatado com R$ e duas casas decimais) e os detalhes do 
# produto que saiu mais caro na conta final.
def calcular_compra(lista):
    soma = 0
    maior = 0
    produto = 0

    for i in lista:
        codigo = i[0]
        quantidade = i[1]
        preco = i[2]
        total = quantidade * preco
        soma = soma + total
        if total > maior:
            maior = total
            produto = codigo
    return soma, (produto, maior)

def main():
    carrinho = [
        (101, 2, 15.50),
        (102, 3, 20.00),
        (103, 1, 100.00),
        (104, 4, 5.00)
    ]
    total, caro = calcular_compra(carrinho)
  
    print(f"total da compra: R$ {total:.2f}")
    print("produto mais caro:", caro[0])
    print(f"valor do produto: R$ {caro[1]:.2f}")
main()
