---
author: Rodrigo Eloy e Leandra Silva
---

# Anonymous Cents
Projeto para a disciplina de Laboratório de Organização e Arquitetura de Computadores(LOAC).

## Objetivo do projeto
Tendo em vista proteger a privacidade dos alunos as notas (centavos) da disciplina são registradas nas contas dos alunos de LOAC nos computadores localizados no LCC3, todavia existem diversos problemas que esse fato acarreta para os alunos:

1. O acesso (remoto principalmente) desses centavos não é instintivo, uma vez que é necessário acessar por meio de linha de comando com ssh;
2. Devido a problemas de infraestrutura do prédio em que o LCC3 está localizado o acesso aos computadores ficou inviável, acarretando na falta de informação acerca das notas de cada aluno.

Tendo isso em criamos o AnonymousCents que cria apelidos para os e-mails dos alunos e gera planilhas para o professor cadastrar os centavos de cada um, fazendo com que os problema previamente citados sejam apagados.

## Como executar o projeto
---
### Pré-requisitos
1. Python 3 - Acesse esse link para [baixar e instalar o python](https://www.python.org/downloads/);
2. Pip - Clique nesse link para [baixar e instalar o pip](https://pip.pypa.io/en/stable/installing/);
3. XlsxWriter, uma Biblioteca python para manipular planilhas. pode ser instalado da seguinte forma. Para instalar essa biblioteca execute o seguinte comando no terminal: `pip install XlsxWriter`.

---
Siga o passo-a-passo a seguir para executar o projeto


1. Crie uma arquivo `emails.py`:

```
touch emails.py
```

2. Abra o arquivo e adicione os e-mails que você quer criar os apelidos e adicione em uma lista de emails no seguinte formato:

```
emails = ['email01', 'email02', 'email03']
```

3. Execute o script `anonymous_cents.py`:

```
python3 anonymous_cents.py
```

