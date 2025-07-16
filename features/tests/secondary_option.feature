# Created by porter at 7/16/25
Feature: Secondary deals test
  # Enter feature description here

  Scenario: User can open the Secondary deals page and go through the pagination
    Given Open the main page
    When Log in to the page
    When Click the Secondary option on the left side menu
    Then Verify the correct page opens
    Then Go to the final page using the pagination button
    Then Go to the first page using the pagination button