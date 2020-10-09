import os 
from colorama import Fore
from src.scripts.util.manipula_planilhas import cria_planilhas
from src.scripts.util.verificadores import verifica_existencia_identificadores
from src.scripts.util.manipular_json import abre_json

def inicia_sistema():
    
    if os.path.exists('src/data/emails.txt'):
        cria_planilhas()
        print(Fore.GREEN + '\nPlanilhas criadas e cadastradas!')

    else:
        print(Fore.RED + '''
---------------------------
Arquivo emails.txt não identificado.
Você precisa criar esse arquivo e preenche-lo com os e-mails dos alunos, cada aluno em uma linha.
Finalize o sistema, adicione o arquivo e inicie novamente o sistema.
---------------------------
''')

def salva_tokens():
    if verifica_existencia_identificadores():
        token_centavos = str(input('\n> Insira aqui o identificador da planilha de centavos: '))
        token_apelidos = str(input('> Insira aqui o identificador da planilha de e-mail e apelidos: '))

        env = open('.env', 'w')
        env.write(f'''TOKEN_CENTAVOS={token_centavos}\nTOKEN_APELIDOS={token_apelidos}''')
        env.close()
