@fixture.browser.chrome
Feature: Google search
  As a user
  I'd like to search for some phrase
  to get new information about it

  Scenario:  a user can search for a phrase
    Given a user visit google
    When the user searches for the "behave python" phrase
    Then one of the results contains: "Welcome to behave"

  Scenario:  a user can search for a very long phrase
    Given a user visit google
    When the user searches for the:
          """
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua.
          """
    Then one of the results contains: "Wikipedia"