import os
import json
import random
from colorama import Fore
from src.scripts.util.manipular_json import (grava_json, abre_json)

PATH_DICIONAIO_APELIDOS = 'src/data/dict_emails_apelidos.json'

def cria_dicionario_apelidos(emails):
    for email in emails:
        adiciona_email_dict_apelidos(email)

    return abre_json(PATH_DICIONAIO_APELIDOS)

def gera_apelido_sem_duplicidade(apelidos):
    apelido = str(random.randint(1000, 3000))

    if apelido in apelidos:
        apelido = gera_apelido_sem_duplicidade(apelidos)

    return apelido

def acessa_dicionario_apelidos():
    if os.path.exists(PATH_DICIONAIO_APELIDOS):
        dict_apelidos = abre_json(PATH_DICIONAIO_APELIDOS)
        return dict_apelidos

    return {}

def adiciona_email_dict_apelidos(email):
    dict_apelidos = acessa_dicionario_apelidos()
    apelido = gera_apelido_sem_duplicidade(dict_apelidos)

    if email not in dict_apelidos:
        dict_apelidos[email] = apelido
        grava_json(PATH_DICIONAIO_APELIDOS, dict_apelidos)
        return (email, apelido)

    print(Fore.RED + f'\nO e-mail {email} já está cadastrado no sistema.')
    return (None, None)