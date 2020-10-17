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

* O acesso (remoto principalmente) desses centavos não é intuitivo, uma vez que é necessário acessar por meio de linha de comando com ssh;
* Devido a problemas de infraestrutura do prédio em que o LCC3 está localizado o acesso aos computadores ficou inviável, acarretando na falta de informação acerca das notas de cada aluno.

:bulb: Tendo isso em vista, criamos o **AnonymousCents** que possui as seguintes ***funcionalidades***:

## :gear: Funcionalidades 

 * :1234: produz apelidos numéricos a partir dos emails dos alunos; 

 * :outbox_tray: envia o apelido automaticamente para o próprio email do aluno;
 
 * :bookmark_tabs: gera de forma automática duas planilhas Google Sheets, sendo elas: 
 
    * uma planilha de acesso *exclusivo* apenas para o professor composta pelos emails dos alunos e o seu respectivo apelido;

    * uma segunda planilha (*centavos.xlsx*) sendo esta acessível pelos alunos e contendo todos os apelidos e os seus respectivos centavos que serão registrados pelo professor, fazendo com que os problemas previamente citados sejam extintos.

* :arrow_lower_right: cadastra um único email, realiza o envio do apelido e faz a adição em ambas planilhas;
