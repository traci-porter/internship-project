# Created by porter at 6/20/25
Feature: Test for Target Terms and Conditions
  # Enter feature description here

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open sign in page
    When Store original window
    And Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    Then User can close new window and switch back to original
    # Enter steps here