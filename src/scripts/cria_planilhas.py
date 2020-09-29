from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font, Alignment
import random

PATH_PLANILHA_CENTAVOS = 'src/data/centavos.xlsx'
PATH_PLANILHA_APELIDOS = 'src/data/apelidos.xlsx'

def cria_planilhas(emails):
    planilha_centavos, pagina_planilha_centavos = cria_planilha_centavos()
    planilha_apelidos, pagina_planilha_apelidos = cria_planilha_apelidos()

    emails_e_apelidos = cria_dicionario_apelidos(emails)

    indice = 2
    for (email, apelido) in emails_e_apelidos.items():
        coluna_a = f'A{indice}'
        coluna_b = f'B{indice}'

        pagina_planilha_centavos[coluna_a] = apelido

        pagina_planilha_apelidos[coluna_a] = email
        pagina_planilha_apelidos[coluna_b] = apelido
        indice += 1

    planilha_centavos.save(filename=PATH_PLANILHA_CENTAVOS)
    planilha_apelidos.save(filename=PATH_PLANILHA_APELIDOS)

    lista_emails = emails_e_apelidos.keys()
    print(f"\nOs emails estão sendo enviados para: \n{list(lista_emails)}\n")
    return emails_e_apelidos

def cria_planilha_centavos():
    planilha_centavos = Workbook()
    pagina_planilha_centavos = planilha_centavos.active
    pagina_planilha_centavos['A1'] = 'Apelido'

    return (planilha_centavos, pagina_planilha_centavos)

def cria_planilha_apelidos():
    planilha_apelidos = Workbook()
    pagina_planilha_apelidos = planilha_apelidos.active
    # TODO: Alterar a largura das colunas
    # pagina_planilha_apelidos.column_dimensions.auto_size = True
    pagina_planilha_apelidos['A1'] = 'Email'
    pagina_planilha_apelidos['B1'] = 'Apelido'

    return (planilha_apelidos, pagina_planilha_apelidos)

def cria_dicionario_apelidos(emails):
    dict_apelidos = {}
    for email in emails:
        apelido = gera_apelido_sem_duplicidade(dict_apelidos.values())
        dict_apelidos[email] = apelido
    return dict_apelidos


def gera_apelido_sem_duplicidade(apelidos):
    apelido = random.randint(1000, 3000)
    if apelido in apelidos:
        return gera_apelido_sem_duplicidade(apelidos)
    return str(apelido)


