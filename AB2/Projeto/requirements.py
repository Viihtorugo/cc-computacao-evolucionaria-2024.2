tabela = {
    'q':1, 'w':6, 'e':7, 'r':6, 't':5, 'y':2, 'u':3, 'i':8, 'o':9, 'p':4,
    'á':3, 'ã':4, 'a':2, 's':5, 'd':8, 'f':7, 'g':4, 'h':1, 'j':4, 'k':7, 'l':8,
    'ç':5, 'é':2, 'í':3, 'z':3, 'x':4, 'c':9, 'v':8, 'b':3, 'n':2, 'm':5,
    'ó':6, 'õ':7, 'ô':6, 'â':1, 'ê':2
}

def valor_nome(nome):
    return sum(tabela.get(letra.lower(), 0) for letra in nome)

def limite_disciplinas(nome):
    print(valor_nome(nome) % 3)
    return {0:10, 1:8, 2:6}[valor_nome(nome) % 3]

def ritmo_conclusao(nome):
    print(valor_nome(nome) % 3)
    return {0:"menor tempo possível", 1:"maior tempo possível", 2:"tempo médio"}[valor_nome(nome) % 3]

def escolha_enfase(nome):
    print(valor_nome(nome) % 3)
    return {0:"ênfase desejada", 1:"ênfase que reduz tempo", 2:"sem ênfase"}[valor_nome(nome) % 3]

def criterio_disciplinas(nome):
    return {
        0:"menos dias possíveis",
        1:"mesmo turno",
        2:"máx. 3 por dia, ir todos os dias"
    }[valor_nome(nome) % 3]

def analisar_aluno(nomes):
    nomes = nomes.split()
    circular = nomes * 3

    primeiro = circular[0]
    proximo1 = circular[1]
    proximo2 = circular[2]
    proximo3 = circular[3]

    print("Nome analisado:", primeiro)
    print("Limite de disciplinas/semestre:", limite_disciplinas(primeiro))
    print("Ritmo de conclusão:", ritmo_conclusao(proximo1))
    print("Ênfase escolhida:", escolha_enfase(proximo2))
    print("Critério de escolha de disciplinas:", criterio_disciplinas(proximo3))

analisar_aluno("Ruan Tenório Melo")