import os
from colorama import Fore
from decouple import config

def verifica_existencia_identificadores():
    dict_bool = {'s': True, 'n': False}

    sobrescrever = True
    if os.path.exists('.env') and config('TOKEN_CENTAVOS', default=None) is not None and config('TOKEN_APELIDOS', default=None) is not None:
        sobrescrever = str(input('\nJá existem idenficadores registrados, deseja sobrescreve-los? (S/N) ')).strip()

        if sobrescrever.lower() in dict_bool:
            sobrescrever = dict_bool[sobrescrever.lower()]

        else:
            print(Fore.YELLOW + '\n>> Você deve selecionar as opções "S" ou "N"')
            sobrescrever = verifica_existencia_identificadores()

    return sobrescrever

def verifica_existencia_emails_cadastrados():
    dict_bool = {'s': True, 'n': False}

    sobrescrever = True
    if os.path.exists('src/data/dict_emails_apelidos.json'):
        sobrescrever = str(input('\nJá existem apelidos apelidos e e-mails cadastrados, deseja sobrescreve-los? (S/N) ')).strip()

        if sobrescrever.lower() in dict_bool:
            sobrescrever = dict_bool[sobrescrever.lower()]

        else:
            print(Fore.YELLOW + '\n>> Você deve selecionar as opções "S" ou "N"')
            sobrescrever = verifica_existencia_emails_cadastrados()

    return sobrescrever
