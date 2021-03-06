import os
from colorama import Fore
from decouple import config


DICTO_BOOL = {'s': True, 'n': False}

def verifica_existencia_identificadores():
    sobrescrever = True

    if (not os.path.exists('.env')) or config('TOKEN_CENTAVOS', default=None) is None or config('TOKEN_APELIDOS', default=None) is None:
        return sobrescrever

    sobrescrever = str(input('\nJá existem idenficadores registrados, deseja sobrescreve-los? (S/N) ')).strip().lower()

    if sobrescrever in DICTO_BOOL:
        sobrescrever = DICTO_BOOL[sobrescrever]

    else:
        print(Fore.YELLOW + '\n>> Você deve selecionar as opções "S" ou "N"')
        sobrescrever = verifica_existencia_identificadores()

    return sobrescrever

def verifica_existencia_emails_cadastrados():
    sobrescrever = True
    if os.path.exists('src/data/dict_emails_apelidos.json'):
        sobrescrever = str(input('\nJá existem apelidos e e-mails cadastrados, deseja sobrescreve-los? (S/N) ')).strip().lower()

        if sobrescrever in DICTO_BOOL:
            sobrescrever = DICTO_BOOL[sobrescrever]

        else:
            print(Fore.YELLOW + '\n>> Você deve selecionar as opções "S" ou "N"')
            sobrescrever = verifica_existencia_emails_cadastrados()

    return sobrescrever

def verifica_inicializacao_sistema():
    if not os.path.exists('src/data/dict_emails_apelidos.json'):
        print(Fore.RED + '\n>> Aparentemente o sistema ainda não foi iniciado, escolha a opção 1 para inicia-lo antes de realizar qualquer outra ação. <<')
        return False
    
    return True