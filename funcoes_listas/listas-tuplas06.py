# 6 - Sistema de Alerta de Manutenção de Frota: Um ônibus transmite diariamente a 
# quilometragem percorrida. Você receberá uma lista com esses trajetos diários e o limite 
# de quilometragem para a revisão do motor. 
# Instituto Federal de Mato Grosso do Sul 
# Lista de Exercícios 
# Retorno exigido: A quilometragem total acumulada, o dia (índice da lista) em 
# que o limite foi ultrapassado, e um booleano (True ou False) indicando se o 
# ônibus precisa ser recolhido imediatamente. 

def verificar_revisao(lista, limite):
    soma = 0
    dia = -1
    for i in range(len(lista)):
        soma = soma + lista[i]
        if soma > limite and dia == -1:
            dia = i

    if dia != -1:
        alerta = True
    else:
        alerta = False
    return soma, dia, alerta

def main():
    trajetos = [150, 200, 180, 250, 300, 100]
    limite = 700
    total, dia, alerta = verificar_revisao(trajetos, limite)
  
    print("quilometragem total:", total)
  
    if alerta:
        print("limite ultrapassado no dia:", dia)
        print("ônibus precisa ser recolhido")
    else:
        print("limite ainda nao ultrapassado")

main()
