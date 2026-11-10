# 10 - Decodificador de Sinais de Satélite: Um satélite envia pacotes de dados como uma 
# lista de bits (0s e 1s). Um pacote de informação válido é sempre sinalizado pelo padrão 
# exato de um 1 seguido imediatamente por dois 0s. 
# Retorno exigido: O número total de pacotes válidos detectados e uma lista de 
# índices marcando onde cada pacote válido começa. 

def decodificar(lista):
    cont = 0
    indices = []
    for i in range(len(lista) - 2):
        if lista[i] == 1 and lista[i+1] == 0 and lista[i+2] == 0:
            cont = cont + 1
            indices.append(i)
    return cont, indices

def main():
    sinais = [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1]
    cont, indices = decodificar(sinais)
  
    print("pacotes encontrados:", cont)
    print("indices dos pacotes:", indices)

main()
