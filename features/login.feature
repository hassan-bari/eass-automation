Feature: Login Functionality

  Scenario: User logs in with valid credentials
    Given the user is on the login page
    When the user enters valid username and password
    Then the user should either be successfully logged in or see the another session page

