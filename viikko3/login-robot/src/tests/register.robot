*** Settings ***
Resource  resource.robot
Test Setup  Input New Command and Create User


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  pekka  pekka123
    Output Should Contain  New user registered

*** Keywords ***
Input New Command and Create User
    Input New Command
    Create User  sonja  sonja123

*** Test Cases ***
Register With Already Taken Username And Valid Password
    Input Credentials   sonja  sonja123
    Output Should Contain  User with username sonja already exists

*** Test Cases ***
Register With Too Short Username And Valid Password
    Input Credentials  so  sonja123
    Output Should Contain  Username must be at least 3 characters long and include only characters a-z

*** Test Cases ***
Register With Enough Long But Invald Username And Valid Password
    Input Credentials  123  sonja123
    Output Should Contain  Username must be at least 3 characters long and include only characters a-z

*** Test Cases ***
Register With Valid Username And Too Short Password
    Input Credentials  testi  123
    Output Should Contain  Password must be at least 8 characters long and it can't include only letters

*** Test Cases ***
Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  testi  testitesti
    Output Should Contain  Password must be at least 8 characters long and it can't include only letters
