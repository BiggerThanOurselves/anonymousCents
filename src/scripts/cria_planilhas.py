from decouple import config
import json
import random

def cria_planilhas():
    emails = open('src/data/emails.txt')
    lines = emails.readlines()
    lista_emails = [line.rstrip(' \n') for line in lines if line.rstrip(' \n') != '']

    dict_apelidos = cria_dicionario_apelidos(lista_emails)

    # print(config('TOKEN_CENTAVOS'))
    # Adicionar os métodos 

    
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


