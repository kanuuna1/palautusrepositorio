*** Settings ***
Library  ../AppLibrary.py
Test Setup  Input New Command

*** Keywords ***
Input Login Command
    Input  login

Input Credentials
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Run Application

Input New Command
    Input  new