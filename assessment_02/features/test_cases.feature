Feature: Login functionality

  Scenario: Successful login with valid credentials
    Given I open the Pickaboo login page
    When I enter valid credentials
    And I click on the login button
    Then I should be logged in successfully
    And I close the browser

  Scenario: Login with invalid credentials
    Given I open the Pickaboo login page
    When I enter invalid credentials
    And I click on the login button
    Then I should see an error message
    And I close the browser
