# 4 - Em um motor gráfico, os obstáculos circulares são uma lista de tuplas (pos_x, pos_y, 
# raio). Você recebe também a tupla do jogador (jog_x, jog_y, jog_raio). 
# A colisão ocorre se a distância entre os centros (use a soma das diferenças absolutas de 
# X e Y como simplificação) for menor que a soma dos raios. 
# Retorno Exigido: Um booleano True ou False indicando se o jogador colidiu com 
# algum obstáculo e a quantidade exata de obstáculos com os quais ele está colidindo 
# simultaneamente. 
# Na Main: Defina uma lista com vários obstáculos espalhados pelo mapa e uma variável 
# separada para as coordenadas do jogador, forçando uma posição onde ele encoste em 
# pelo menos dois obstáculos ao mesmo tempo. Chame a função e exiba uma mensagem 
# de status ("Impacto Detectado!" ou "Caminho Livre") e a quantidade de objetos 
# atingidos.

def verificar_colisao(lista, jogador):
    cont = 0
    jog_x = jogador[0]
    jog_y = jogador[1]
    jog_raio = jogador[2]

    for i in lista:
        pos_x = i[0]
        pos_y = i[1]
        raio = i[2]

        distancia = abs(jog_x - pos_x) + abs(jog_y - pos_y)
        if distancia < jog_raio + raio:
            cont = cont + 1
    if cont > 0:
        return True, cont
    else:
        return False, cont

def main():
    obstaculos = [
        (5, 5, 3),
        (8, 5, 3),
        (20, 20, 2),
        (30, 10, 4)
    ]
    jogador = (6, 5, 3)
    colisao, cont = verificar_colisao(obstaculos, jogador)
    if colisao:
        print("Impacto detectado!")
    else:
        print("Caminho livre")
    print("Qtde de objetos atingidos:", cont)
main()
