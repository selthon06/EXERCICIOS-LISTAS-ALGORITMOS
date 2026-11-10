# 7 - Análise de Turbulência em Voo: Os sensores de um avião registram a altitude a cada 
# minuto (lista de números). Uma turbulência severa é caracterizada por uma queda de 
# altitude maior que 500 metros em um único minuto. 
# Retorno exigido: True ou False se houve turbulência severa, e a maior queda 
# registrada em um minuto durante todo o voo. 


def analisar_altitude(lista):
    maior = 0
    alerta = False

    for i in range(1, len(lista)):
        queda = lista[i-1] - lista[i]
        if queda > maior:
            maior = queda
        if queda > 500:
            alerta = True
    return alerta, maior

def main():
    altitude = [5000, 4800, 4500, 3800, 3500, 3000]

    alerta, maior = analisar_altitude(altitude)

    print("turbulencia severa:", alerta)
    print("maior queda:", maior, "metros")

main()
