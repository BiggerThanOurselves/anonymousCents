import os
import random
import gspread
from colorama import Fore
from decouple import config
from src.scripts.util.envia_email import envia_email
from src.scripts.util.verificadores import verifica_existencia_emails_cadastrados
from src.scripts.util.dicionario_apelidos import cria_dicionario_apelidos

def inicia_servidor_planilhas(identificador_planilha):

    server_gc = gspread.service_account(filename='credentials.json')
    sheet_google = server_gc.open_by_key(identificador_planilha)
    pag_planilha = sheet_google.sheet1
    
    return (sheet_google, pag_planilha)

def cria_planilhas():

    emails = open('src/data/emails.txt')
    linhas = emails.readlines()

    existe_emails_cadastrados = verifica_existencia_emails_cadastrados()

    if not existe_emails_cadastrados:
        return

    lista_emails = [linha.rstrip(' \n') for linha in linhas if linha.rstrip(' \n') != '']
    dict_apelidos = cria_dicionario_apelidos(lista_emails)

    planilha_centavos, pagina_centavos = inicia_servidor_planilhas(str(config('TOKEN_CENTAVOS')))
    pagina_centavos.clear()
    _, pagina_emails_apelidos = inicia_servidor_planilhas(str(config('TOKEN_APELIDOS')))
    pagina_emails_apelidos.clear()

    for email, apelido in dict_apelidos.items():
        try:
            planilha_centavos.share(email, perm_type='user', role='reader')
            add_planilha([apelido], pagina_centavos)

            add_planilha([email, apelido], pagina_emails_apelidos)
        except:
            print(Fore.RED + f'\n>> O e-mail {email} foi considerado uma e-mail invalido')

    envia_email()

def add_email_unico(email, apelido):
    _, pagina_centavos = inicia_servidor_planilhas(str(config('TOKEN_CENTAVOS')))
    _, pagina_emails_apelidos = inicia_servidor_planilhas(str(config('TOKEN_APELIDOS')))

    add_planilha([apelido], pagina_centavos)
    add_planilha([email, apelido], pagina_emails_apelidos)

def add_planilha(lista, pagina_adicionada):
    adiciona = lista
    pagina_adicionada.append_row(adiciona)



