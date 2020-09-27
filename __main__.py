from src.scripts.envia_email import envia_email
from src.scripts.anonymous_cents import cria_planilhas

with open('./src/data/emails.py', 'r') as e_mails:
    emails_passados = e_mails.read()
    exec(emails_passados)

if __name__ == '__main__':
    emails_apelidos = cria_planilhas(emails)
    envia_email(emails_apelidos)
