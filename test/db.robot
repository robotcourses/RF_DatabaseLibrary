*** Settings ***
Resource    ../base.resource
Test Tags    db

*** Test Cases ***
Exemplo 1: SELECT

    ${sql}  Sql Select Users
    ${result}  Execute Query    ${sql}

    ${sql}  Sql Select Users  id=1
    ${result}  Execute Query    ${sql}

Exemplo 4: INSERT

    ${sql}  Sql Insert User    nome=Joaquina    email=joaquina@teste.com.br    idade=36
    Execute SQL    ${sql}

Exemplo 2: UPDATE
   
    ${sql}  Sql Update User    id=1  nome=Jose
    Execute SQL    ${sql}

Exemplo 3: DELETE

    ${sql}  Sql Delete Users  id=2
    Execute SQL    ${sql}
