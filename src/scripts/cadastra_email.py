from src.scripts.util.dicionario_apelidos import adiciona_email_dict_apelidos
from src.scripts.util.envia_email import envia_email_unico

def cadastra_email():
    email = str(input('Digite o e-mail que será cadastrado: '))
    email_cadastrado, apelido = adiciona_email_dict_apelidos(email)
    print(email_cadastrado, apelido)
    envia_email_unico(email_cadastrado, apelido)

