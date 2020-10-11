import os 
from colorama import Fore
from src.scripts.util.manipula_planilhas import cria_planilhas
from src.scripts.util.verificadores import verifica_existencia_identificadores
from src.scripts.util.manipular_json import abre_json

ARQUIVO_VAZIO = '''
>> Arquivo emails.txt vazio.
> Você precisa preenche-lo com os e-mails dos alunos, cada aluno em uma linha.
'''

def inicia_sistema():

    if os.path.getsize('src/data/emails.txt') > 0:
        salva_tokens()
        cria_planilhas()
        print(Fore.GREEN + '\nPlanilhas criadas e cadastradas!')

    else:
        print(Fore.RED + ARQUIVO_VAZIO)

def salva_tokens():
    if verifica_existencia_identificadores():
        token_centavos = str(input('\n> Insira aqui o identificador da planilha de centavos: '))
        token_apelidos = str(input('> Insira aqui o identificador da planilha de e-mail e apelidos: '))

        env = open('.env', 'w')
        env.write(f'''TOKEN_CENTAVOS={token_centavos}\nTOKEN_APELIDOS={token_apelidos}''')
        env.close()

