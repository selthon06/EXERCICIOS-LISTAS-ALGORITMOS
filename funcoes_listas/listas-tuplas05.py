# 5 - Controle de Qualidade Agrícola: Uma fazenda colhe maçãs e as classifica pelo peso 
# (em gramas). Você receberá a lista de pesos, o peso mínimo para exportação e o peso 
# máximo. 
# Retorno exigido: Uma lista contendo os pesos aprovados, uma segunda lista com 
# os pesos descartados, e a porcentagem de perda da safra (número float). 

def classificar(pesos, minimo, maximo):
    aprovados = []
    descartados = []

    for i in pesos:
        if i >= minimo and i <= maximo:
            aprovados.append(i)
        else:
            descartados.append(i)

    perda = (len(descartados) / len(pesos)) * 100

    return aprovados, descartados, perda

def main():
    pesos = [120, 150, 180, 90, 200, 110, 250, 160]
    minimo = 100
    maximo = 200

    aprovados, descartados, perda = classificar(pesos, minimo, maximo)

    print("pesos aprovados:", aprovados)
    print("pesos descartados:", descartados)
    print(f"perda da safra: {perda:.2f}%")

main()
