from src.scripts.util.dicionario_apelidos import adiciona_email_dict_apelidos
from src.scripts.util.envia_email import envia_email_unico
from src.scripts.util.manipula_planilhas import add_email_unico

def cadastra_email():
    email = str(input('Digite o e-mail que será cadastrado: '))
    email_cadastrado, apelido = adiciona_email_dict_apelidos(email)

    if email_cadastrado is not None:
        envia_email_unico(email_cadastrado, apelido)
        add_email_unico(email_cadastrado, apelido)