Feature: Argaam - User Authentication

  Background: Validate Credentials
    Given I navigate to "home" page
    Then I verify the "home" page as "normal" user

  @login
  Scenario: User Authentication
    When I login as a real user
    Then I verify the "home" page as "real" user
