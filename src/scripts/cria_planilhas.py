import os
import random
import gspread
from colorama import Fore
from decouple import config
from src.scripts.util.envia_email import envia_email
from src.scripts.util.verificadores import verifica_existencia_emails_cadastrados
from src.scripts.util.dicionario_apelidos import cria_dicionario_apelidos

def cria_planilhas():
    emails = open('src/data/emails.txt')
    linhas = emails.readlines()

    existe_emails_cadastrados = verifica_existencia_emails_cadastrados()

    if not existe_emails_cadastrados:
        return

    lista_emails = [linha.rstrip(' \n') for linha in linhas if linha.rstrip(' \n') != '']
    dict_apelidos = cria_dicionario_apelidos(lista_emails)

    cria_planilha_apelidos_emails(dict_apelidos, str(config('TOKEN_APELIDOS')))
    cria_planilha_apelidos(dict_apelidos, str(config('TOKEN_CENTAVOS')))
    envia_email()


def cria_planilha_apelidos_emails(dict_email_apelido, identificador_planilha):

    server_gc = gspread.service_account(filename='credentials.json')
    sheet_google = server_gc.open_by_key(identificador_planilha)
    pag_planilha = sheet_google.sheet1

    for email, apelido in dict_email_apelido.items():
        add_email_apelido = [email, apelido]
        pag_planilha.append_row(add_email_apelido)

def cria_planilha_apelidos(dict_email_apelido, identificador_planilha):

    server_gc = gspread.service_account(filename='credentials.json')
    sheet_google = server_gc.open_by_key(identificador_planilha)
    pag_planilha = sheet_google.sheet1

    for apelido in dict_email_apelido.values():
        add_apelido = [apelido]
        pag_planilha.append_row(add_apelido)
