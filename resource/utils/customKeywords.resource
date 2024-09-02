*** Settings ***
Resource    ../../base.resource

*** Keywords ***
Execute Query
    [Arguments]  ${selectStatement}
    [Teardown]   Disconnect From Database  alias=rc
    [Timeout]    5s

    Connect RC Base
    ${result}  Query    ${selectStatement}
    RETURN  ${result}


Execute SQL
    [Arguments]  ${sqlString}
    [Teardown]   Disconnect From Database  alias=rc
    [Timeout]    5s

    Connect RC Base
    Execute Sql String    ${sqlString}