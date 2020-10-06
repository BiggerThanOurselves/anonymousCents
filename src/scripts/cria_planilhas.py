import os
import json
import random
from decouple import config
from colorama import Fore
import gspread

def cria_planilhas():
    emails = open('src/data/emails.txt')
    linhas = emails.readlines()

    existe_emails_cadastrados = verifica_existencia_emails_cadastrados()

    if not existe_emails_cadastrados:
        return

    lista_emails = [linha.rstrip(' \n') for linha in linhas if linha.rstrip(' \n') != '']
    dict_apelidos = cria_dicionario_apelidos(lista_emails)

def verifica_existencia_emails_cadastrados():
    dict_bool = {'s': True, 'n': False}

    if os.path.exists('src/data/dict_emails_apelidos.json'):
        sobrescrever = str(input('\nJá existem apelidos apelidos e e-mails cadastrados, deseja sobrescreve-los? (S/N) '))

        if sobrescrever.lower() in dict_bool:
            return dict_bool[sobrescrever.lower()]

    print(Fore.YELLOW + '\n>> Você deve selecionar as opções "S" ou "N"')
    verifica_existencia_emails_cadastrados()

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
    
    with open('src/data/dict_emails_apelidos.json', 'w') as json_file:
        json.dump(dict_apelidos, json_file)

    return dict_apelidos


def gera_apelido_sem_duplicidade(apelidos):
    apelido = random.randint(1000, 3000)
    if apelido in apelidos:
        return gera_apelido_sem_duplicidade(apelidos)
    return str(apelido)


