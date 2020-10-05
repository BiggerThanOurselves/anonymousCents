import os 
from colorama import (init, Fore, Style)
from src.scripts.cria_planilhas import cria_planilhas
def salva_tokens():
    token_centavos = str(input('\nInsira aqui o identificador da planilha de centavos: '))
    token_apelidos = str(input('Insira aqui o identificador da planilha de e-mail e apelidos: '))

    with open('.env', 'w') as env:
        env.write(f'TOKEN_CENTAVOS = {token_centavos}')
        env.write('\n')
        env.write(f'TOKEN_APELIDOS = {token_apelidos}')
        env.close()

def verifica_existencia_emails():
    if not os.path.exists('src.data.emails.txt'):
        print(Fore.RED + 
        '''Arquivo emails.txt não identificado.
        Você precisa criar esse arquivo e preenche-lo com os e-mails dos alunos, cada aluno em uma linha.''')


def inicia_sistema():
    salva_tokens()

    if not os.path.exists('src/data/emails.txt'):
        print(Fore.RED + '''
---------------------------
Arquivo emails.txt não identificado.
Você precisa criar esse arquivo e preenche-lo com os e-mails dos alunos, cada aluno em uma linha.
Finalize o sistema, adicione o arquivo e inicie novamente o sistema.
---------------------------
''')
    else:
        cria_planilhas()
