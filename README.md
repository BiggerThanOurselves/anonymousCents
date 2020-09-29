---
author: Rodrigo Eloy e Leandra Silva
---

# 🕵🏼‍♂️ Anonymous Cents 🕵🏽‍♀️
Projeto para a disciplina de Laboratório de Organização e Arquitetura de Computadores(LOAC).

<div align=center>
    <p><i>E vamos de... centavos</i></p>
    <img src='./src/assets/img/perna-longa.gif'>
</div>

## :dart: Objetivo do projeto
Tendo em vista proteger a privacidade dos alunos as notas (centavos) da disciplina são registradas nas contas dos alunos de LOAC nos computadores localizados no LCC3, todavia existem diversos problemas que esse fato acarreta para os alunos:

1. O acesso (remoto principalmente) desses centavos não é intuitivo, uma vez que é necessário acessar por meio de linha de comando com ssh;
2. Devido a problemas de infraestrutura do prédio em que o LCC3 está localizado o acesso aos computadores ficou inviável, acarretando na falta de informação acerca das notas de cada aluno.

Tendo isso em vista, criamos o **AnonymousCents** que possui as seguintes ***funcionalidades***:

 * produz apelidos a partir dos e-mails dos alunos; 

 * envia o apelido automaticamente para o próprio email do aluno;

 * gera uma planilha para o professor com os emails dos alunos e o seu respectivo apelido;

 * gera uma segunda planilha (*centavos.xlsx*) que será acessível pelos alunos, onde o professor irá cadastrar os centavos de cada um, fazendo com que os problemas previamente citados sejam extintos.

## :arrow_forward: Como executar o projeto
---
### :inbox_tray: Pré-requisitos
1. Python 3 - Acesse esse link para [baixar e instalar o python](https://www.python.org/downloads/);
2. Pip - Clique nesse link para [baixar e instalar o pip](https://pip.pypa.io/en/stable/installing/);
3. Openpyxl, uma Biblioteca python para manipular planilhas. pode ser instalado da seguinte forma. Para instalar essa biblioteca execute o seguinte comando no terminal: `$ pip install openpyxl`.

> :warning: caso o comando acima não funcione, tente `pip3 install openpyxl`

---
:pencil: Siga o passo-a-passo a seguir para executar o projeto


1. Na pasta ***data*** crie um arquivo `emails.py`:

    ```
    $ cd data
    $ touch emails.py
    ```

2. Abra o arquivo e adicione os e-mails que você deseja que sejam criados apelidos e adicione em uma lista de emails no seguinte formato:

    ```
    emails = ['email01@gmail.com', 'email02@ccc.ufcg.edu.br', 'email03@computacao.ufcg.edu.br']
    ```

3. Execute o script `__main__.py`:

    ```
    $ python3 __main__.py
    ```

4. Ao executar o script, serão pedidas as seguintes informações: 

    ```
    $ Informe o e-mail do remetente: 
   
    $ Informe a senha de e-mail do remetente:
    ```
    > :warning: o cursor estará travado ao receber sua senha, isto ocorrerá para que sua senha não seja exibida. 

    ```
    $ Digite a mensagem que deseja enviar para os destinatários (sem acentos): 
    
    ```

5. :heavy_check_mark: Após finalizar estes passos, o seu email será enviado para os emails registrados no arquivo `emails.py`.
