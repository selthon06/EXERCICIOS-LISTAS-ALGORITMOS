# 9- Escala Crítica de Plantão Médico: Um hospital fornece uma lista onde cada elemento 
# é uma sublista com os dias do mês em que um médico específico pode trabalhar. O 
# diretor quer saber qual é o dia do mês que tem a menor cobertura de profissionais. 
# Retorno exigido: O dia (número) com a menor quantidade de médicos 
# disponíveis e uma lista com os índices (IDs) dos médicos que farão plantão 
# nesse dia crítico. 

# ==========================================
# EXERCÍCIO 9 — ESCALA DE PLANTAO
# ==========================================

def analisar_escala(lista):
    dias = []

    for i in lista:
        for j in i:
            if j not in dias:
                dias.append(j)
    menor = len(lista) + 1
    dia_menor = 0
    medicos = []

    for i in dias:
        cont = 0
        disponiveis = []
        for j in range(len(lista)):
            if i in lista[j]:
                cont = cont + 1
                disponiveis.append(j)
        if cont < menor:
            menor = cont
            dia_menor = i
            medicos = disponiveis

    return dia_menor, medicos

def main():
    escala = [
        [1, 2, 5, 10],
        [2, 3, 5, 8],
        [1, 3, 8, 10],
        [2, 5, 8, 10]
    ]
    dia, medicos = analisar_escala(escala)

    print("dia com menor cobertura:", dia)
    print("medicos disponiveis:", medicos)

main()
