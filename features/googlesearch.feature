@fixture.browser.chrome
Feature: Google search
  As a user
  I'd like to search for some phrase
  to get new information about it

  Scenario:  a user can search for a phrase
    Given a user visit google
    When the user searches for the "behave python" phrase
    Then one of the results contains: "Welcome to behave"