*** Settings ***
Resource    ../../base.resource

*** Keywords ***
Connect RC Base

    Connect To Database
    ...  alias=rc
    ...  dbapiModuleName=pymysql
    ...  dbName=rc_databaselibrary
    ...  dbUsername=rc_user
    ...  dbPassword=rc_123
    ...  dbHost=localhost
    ...  dbPort=3306