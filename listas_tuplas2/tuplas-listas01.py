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
