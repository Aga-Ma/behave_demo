@fixture.browser.chrome
Feature: Google search
  As a user
  I'd like to search for some phrase
  to get new information about it

  Scenario Outline:  a user can search for a phrases
    Given a user visit google
    When the user searches for the "<search>" phrase
    Then one of the results contains: "<expected result>"

    Examples: BDD topics
      | search            | expected result             |
      | BDD               | Behavior-driven development |
      | Behaviour Testing | Tutorialspoint              |
      | Dan North         | Introducing BDD             |

    Examples: Selenium topics
      | search            | expected result                 |
      | Selenium          | Selenium Tutorial for Beginners |
      | Page Object Model | Design Pattern                  |