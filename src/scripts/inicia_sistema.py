import os 
from decouple import config
from colorama import Fore
from src.scripts.cria_planilhas import cria_planilhas

def salva_tokens():
    
    if verifica_existencia_identificadores():
        token_centavos = str(input('\n> Insira aqui o identificador da planilha de centavos: '))
        token_apelidos = str(input('> Insira aqui o identificador da planilha de e-mail e apelidos: '))

        with open('.env', 'w') as env:
            env.write(f'TOKEN_CENTAVOS = {token_centavos}')
            env.write('\n')
            env.write(f'TOKEN_APELIDOS = {token_apelidos}')
            env.close()

def inicia_sistema():
    if os.path.exists('src/data/emails.txt'):
        salva_tokens()
        cria_planilhas()

    else:
        print(Fore.RED + '''
---------------------------
Arquivo emails.txt não identificado.
Você precisa criar esse arquivo e preenche-lo com os e-mails dos alunos, cada aluno em uma linha.
Finalize o sistema, adicione o arquivo e inicie novamente o sistema.
---------------------------
''')

def verifica_existencia_identificadores():
    dict_bool = {'s': True, 'n': False}

    if config('TOKEN_CENTAVOS') is not None and config('TOKEN_APELIDOS') is not None:
        sobrescrever = str(input('\nJá existem idenficadores registrados, deseja sobrescreve-los? (S/N) '))

        if sobrescrever.lower() in dict_bool:
            return dict_bool[sobrescrever.lower()]
    
        print(Fore.YELLOW + '\n>> Você deve selecionar as opções "S" ou "N"')
        verifica_existencia_identificadores()