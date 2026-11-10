# 2 - Um serviço de streaming tem seu catálogo representado por uma lista de tuplas 
# (titulo_filme, ano_lancamento, genero, avaliacao_usuarios). Você também receberá 
# como parâmetro um genero_alvo (string) e uma nota_corte (float). 
# Você deve extrair dados com base em múltiplos parâmetros de entrada e encontrar o 
# "menor valor" (mais antigo) dentro de um subconjunto específico. 
# Retorno Exigido: Uma lista apenas com os títulos dos filmes que batem com o gênero 
# alvo e possuem nota igual ou superior ao corte, e uma tupla com o (titulo_filme, 
# ano_lancamento) do filme mais antigo dessa lista filtrada. 
# Na Main: Construa uma lista estática com pelo menos 4 filmes misturando gêneros e 
# notas. Defina variáveis para o seu gênero alvo e sua nota de corte. Invoque a função e 
# imprima a lista final de filmes aprovados, seguida de uma mensagem informando qual é 
# o filme mais antigo dentre os que foram filtrados. 

def filtrar_filmes(lista, genero_alvo, nota_corte):
    filmes = []
    antigo = None
    for i in lista:
        titulo = i[0]
        ano = i[1]
        genero = i[2]
        nota = i[3]
      
        if genero == genero_alvo and nota >= nota_corte:
            filmes.append(titulo)
            if antigo == None or ano < antigo[1]:
                antigo = (titulo, ano)
    return filmes, antigo
  
def main():
    lista = [
        ("Interestelar", 2014, "ficção", 9.0),
        ("Avatar", 2009, "ficção", 8.5),
        ("Titanic", 1997, "romance", 8.0),
        ("Matrix", 1999, "ficção", 9.2),
        ("Oppenheimer", 2023, "drama", 8.8)
    ]
    genero = "ficção"
    nota = 8.5
    filmes, antigo = filtrar_filmes(lista, genero, nota)

    print("Filmes aprovados:", filmes)

    if antigo != None:
        print("filme mais antigo:", antigo[0])
        print("ano de lançamento:", antigo[1])
    else:
        print("nenhum filme encontrado")
main()
