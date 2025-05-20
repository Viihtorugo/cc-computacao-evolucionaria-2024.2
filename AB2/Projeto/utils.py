import csv
import random

def ler_ppc(filename):
    materias = []
    with open('materias_ppc_2019.csv', 'r', newline='', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for materia in leitor_csv:
            materia['horas'] = int(materia['horas'])
            materia['pre_requisitos'] = materia['pre_requisitos'].split(',') if materia['pre_requisitos'] else []
            materia['horas'] = int(materia['horas'])
            materia['periodo'] = int(materia['periodo'])
            materia['obrigatorio'] = bool(materia['periodo'])
        
            materias.append(materia)
    return materias


def ler_historico(file: str):
    """
    Lê o arquivo de histórico e retorna um objeto Historico.
    O arquivo deve conter o período, horas flexíveis e os itens do histórico.
    """
    try:
        with open(file, 'r', encoding='utf-8') as arquivo:
            # Itera sobre cada linha do arquivo
            conteudo = arquivo.read()
            conteudo = conteudo.strip()
            linhas = conteudo.split("\n")
          
            # Trata a primeira linha como o período
            periodo = int(linhas[0].strip())
            horas_flexiveis = int(linhas[1].strip())
            historico = {}
            for linha in linhas[2:]:
                # Verifica se a linha não está vazia
                if linha.strip():
                    # Separa os dados da linha
                    dados = linha.split(" ")
                    # Cria um objeto ItemHistorico com os dados
                    historico[dados[0]] = float(dados[1].replace(",", "."))

            return periodo, horas_flexiveis, historico
    
    except FileNotFoundError:
        print("O arquivo não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    
    return None

def busca_materia(materias, codigo: str):
    """
    Busca uma matéria pelo código na lista de matérias.
    
    Args:
        materias (list): Lista de matérias.
        codigo (str): Código da matéria a ser buscada.
    
    Returns:
        Materia: Objeto da classe Materia correspondente ao código, ou None se não encontrado.
    """
    for materia in materias:
        if materia['codigo'] == codigo:
            return materia
    return None


def cria_turmas(materias):
    turmas = []
    
    with open('turmas.csv', 'r', newline='', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for linha in leitor_csv:  
            codigo = linha['codigo']
            horario = linha['horario']
            if not codigo or not horario:
                continue
            turmas.append({'codigo': codigo, 'horario': horario})
    
    for t in turmas:
        # print(t['horario'])
        m_find = busca_materia(materias, t['codigo'])

        if m_find is None:
            print(f"Materia {t['codigo']} não encontrada")
            continue
        
        if m_find:
            i = 0
        
        horarios = []
        while i < len(t['horario']):
            
            l = i
            while t['horario'][i].isdigit():
                i += 1
            dias = int(t['horario'][l:i])

            turno = t['horario'][i]
            i += 1

            l = i
            while i < len(t['horario']) and t['horario'][i].isdigit():
                i += 1
            horas = int(t['horario'][l:i])

            horarios.append({'horas': horas, 'turno': turno, 'dias': dias})
            i += 1
        
        m_find['horario'] = horarios

            # Insere o array de horarios na materia

def gera_individuo(materias_disponiveis):
    """
    Gera um individuo aleatorio com base nas materias disponiveis.
    """
    numeros = [1, 2, 3, 4, 5, 6, 7, 8]
    pesos = [8, 7, 6, 5, 4, 3, 2, 1]  
    numero_sorteado = random.choices(numeros, weights=pesos, k=1)[0]
    genes = random.sample(materias_disponiveis, numero_sorteado)
    return genes



def consulta_materias_disponiveis(materias, historico):
    """
    Consulta as materias disponiveis com base no historico.
    """
    materias_disponiveis = []
    
    for materia in materias:
        if not materia['horario']:
  
            continue
     
        # historico_materia = historico.get(materia['codigo'], None)
        if not materia['codigo'] in historico:
            # Não pagou a materia ainda
            # print(f"Materia {materia['codigo']} não encontrada no historico")
            materias_disponiveis.append(materia)
        else:
            if historico[materia['codigo']] < 5.5: # TODO: mudar isso (caso ele tenha reprovado e passado depois)
                # print(f"Materia {materia['codigo']} reprovada")
                materias_disponiveis.append(materia)
    return materias_disponiveis                                 

def conflito_turno(cromossomo):

    count = 0
    turno = cromossomo[0]['horario'][0]['turno']
    
    for c in cromossomo:
        for i in range(len(c['horario'])):
            if turno != c['horario'][i]['turno']:
                print(f"{cromossomo[0]['nome']} == {c['nome']}")
                print(f"{cromossomo[0]['horario'][0]['turno']} != {c['horario'][i]['turno']}")
                count += 1

    return count

def fitness(cromossomo):
    # Não pode ter choque de horário
    #codigo,nome,horas,pre_requisitos,obrigatorio,periodo,horario
    fit = 0

    for a in cromossomo:
        for b in cromossomo:
            if a != b:
                for ah in a['horario']:
                    for bh in b['horario']:
                        if ah['turno'] == bh['turno']:
                            for a_dias in str(ah['dias']):
                                for b_dias in str(bh['dias']):
                                    if a_dias == b_dias:
                                        for a_horas in str(ah['horas']):
                                            for b_horas in str(bh['horas']):
                                                if a_horas == b_horas:
                                                    print(f"{a['nome']} == {b['nome']}")
                                                    print(ah)
                                                    print(bh)
                                                    fit -= 999

 
        fit -= conflito_turno(cromossomo) * 999

    return fit 