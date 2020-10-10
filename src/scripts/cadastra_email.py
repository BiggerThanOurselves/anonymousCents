from src.scripts.util.dicionario_apelidos import adiciona_email_dict_apelidos

def cadastra_email():
    email = str(input('Digite o e-mail que será cadastrado: '))

    email_cadastrado, apelido = adiciona_email_dict_apelidos(email)

    print(f'{email_cadastrado}, {apelido}')
