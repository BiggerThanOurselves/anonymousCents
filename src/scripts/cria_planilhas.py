from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font, Alignment
import random
import gspread

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

def cria_planilha_apelidos_emails(dict_email_apelido, identificador_planilha):

    server_gc = gspread.service_account(filename= 'credentials.json')
    sheet_google = server_gc.open_by_key(identificador_planilha)
    pag_planilha = sheet_google.sheet1

    for email, apelido in dict_email_apelido.items():
        add_email_apelido = [email, apelido]
        pag_planilha.append_row(add_email_apelido)

def cria_planilha_apelidos(dict_email_apelido, identificador_planilha):

    server_gc = gspread.service_account(filename= 'credentials.json')
    sheet_google = server_gc.open_by_key(identificador_planilha)
    pag_planilha = sheet_google.sheet1

    for apelido in dict_email_apelido.values():
        add_apelido = [apelido]
        pag_planilha.append_row(add_apelido)


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


