*** Settings ***
Resource  resource.robot
Resource  login_resource.robot

Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  sonja
    Set Password  sonja123
    Confirm Password  sonja123
    Submit Credentials
    Registration Should Succeed

Login After Successful Registration
    Go To Login Page
    Set Username  sonja
    Set Password  sonja123
    Submit Login Credentials
    Login Should Succeed

Register With Too Short Username And Valid Password
    Set Username  so
    Set Password  sonja123
    Confirm Password  sonja123
    Submit Credentials
    Registration Should Fail with Message  Username must be at least 3 characters long and include only characters a-z

Login After Failed Registration
    Go To Login Page
    Set Username  so
    Set Password  sonja123
    Submit Login Credentials
    Login Should Fail with Message  Invalid username or password

Register With Valid Username And Invalid Password
    Set Username  pekka
    Set Password  so
    Confirm Password  so
    Submit Credentials
    Registration Should Fail with Message  Password must be at least 8 characters long and it can't include only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  testi
    Set Password  testi123
    Confirm Password  testi321
    Submit Credentials
    Registration Should Fail with Message  Passwords do not match
    



*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Confirm Password
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button  Register

Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
