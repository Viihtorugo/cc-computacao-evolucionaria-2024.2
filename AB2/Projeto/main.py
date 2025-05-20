import csv
from utils import * 


materias = ler_ppc('materias_ppc_2019.csv')
PERIODO_ATUAL, HORAS_FLEXIVEIS, historico = ler_historico('historico.txt')
cria_turmas(materias)
materias_disponiveis = consulta_materias_disponiveis(materias, historico)

MAX_POPULACAO = 10
populacao = []

for i in range(MAX_POPULACAO):
    individuo = gera_individuo(materias_disponiveis)
    populacao.append(individuo)
    print("==============")
    print(fitness(individuo))
    

# for i in range(200):
#     print(f'Iteração {i+1}')

# Crie uma função que leia um arquivo csv e drope todas as colunas, exceto as de codigo e horario
# Ao final salve o novo arquivo com o nome 'turmas.csv'

# def busca_materia(materias, codigo: str) -> Materia:
    
#     for materia in materias:
#         if materia.codigo == codigo:
#             return materia
#     return None

# def ler_ppc(nome_arquivo_csv) -> List[Materia]:
#     """
#     Lê um arquivo CSV e cria objetos da classe Materia.

#     Args:
#         nome_arquivo_csv (str): O nome do arquivo CSV a ser lido.

#     Returns:
#         list: Uma lista de objetos da classe Materia criados a partir do CSV.
#               Retorna uma lista vazia se o arquivo não for encontrado ou estiver vazio.
#     """
#     materias = []
#     try:
#         with open(nome_arquivo_csv, 'r', newline='', encoding='utf-8') as arquivo_csv:
#             leitor_csv = csv.DictReader(arquivo_csv)
#             for linha in leitor_csv:
#                 codigo = linha['codigo']
#                 nome = linha['nome']
#                 horas = int(linha['horas'])
#                 pre_requisitos = linha['pre_requisitos']
#                 obrigatorio = linha['obrigatorio']
#                 periodo = linha['periodo']
                
#                 materia = Materia(codigo, nome, horas, pre_requisitos, obrigatorio, periodo)
#                 materias.append(materia)
#     except FileNotFoundError:
#         print(f"Erro: Arquivo '{nome_arquivo_csv}' não encontrado.")
#     except Exception as e:
#         print(f"Ocorreu um erro ao ler o arquivo CSV: {e}")
#     return materias

# # turmas = [
# #     Turma(
# #         m, f"{random.randint(1,6)}{random.randint(1,6)}{'T' if random.randint(0,1) else 'M'}{random.randint(1,6)}{random.randint(1,6)}"
# #         ) for m in materias
# # ]