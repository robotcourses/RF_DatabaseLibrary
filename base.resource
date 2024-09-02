*** Settings ***
# Bibliotecas
Library    DatabaseLibrary

## Strings SQL
Library    resource/db/userSql.py

# Recursos
Resource    resource/db/connectDatabase.resource

# Utils
Resource    resource/utils/customKeywords.resource