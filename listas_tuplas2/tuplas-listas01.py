# 1 - Uma estufa inteligente possui vários sensores. O microcontrolador envia uma lista 
# de tuplas no formato (id_sensor, temperatura, umidade). As regras de segurança dizem 
# que a temperatura não pode passar de 35°C e a umidade não pode ficar abaixo de 20%. 
# Você precisa rastrear simultaneamente o maior valor de uma variável e o menor de 
# outra, enquanto filtra dados. 
# Retorno Exigido: Uma lista contendo apenas os id_sensor que dispararam algum 
# alarme de perigo, e uma tupla (maior_temperatura, menor_umidade) registrada em todo 
# o período. 
# Na Main: Crie uma lista simulando pelo menos 4 sensores (certifique-se de forçar pelo 
# menos um alerta de temperatura e um de umidade). Chame a função passando essa lista. 
# Imprima no terminal quais sensores entraram em alerta e exiba os picos máximos e 
# mínimos. 
def analisar_sensores(lista):
    alertas = []
    maior = lista[0][1]
    menor = lista[0][2]

    for i in lista:
        id_sensor = i[0]
        temperatura = i[1]
        umidade = i[2]
        if temperatura > maior:
            maior = temperatura
        if umidade < menor:
            menor = umidade
        if temperatura > 35 or umidade < 20:
            alertas.append(id_sensor)
    return alertas, (maior, menor)

def main():
    sensores = [
        (1, 30, 40),
        (2, 38, 35),
        (3, 32, 15),
        (4, 40, 10)
    ]
    alertas, picos = analisar_sensores(sensores)
    print("Sensores em alerta:", alertas)
    print("Maior temperatura:", picos[0])
    print("Menor umidade:", picos[1])

main()
