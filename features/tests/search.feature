# Created by porter at 6/13/25
Feature: Tests for Target Search
  # Enter feature description here

  Scenario: User can search for tea
    Given Open Target main page
    When Search for tea
    Then Verify search worked for tea

  Scenario: Verify that user can see product names and images
    Given Open Target main page
    When Search for Airpods
    Then Verify that every product has a name and an image

  Scenario: User can see favorites tooltip for search results
    Given Open Target main page
    When Search for tea
    And Hover favorites icon
    Then Favorites tooltip is shown

 # Scenario: User can search for a product
 #   Given Open Target main page
 #   When Input 'V8 +Energy Summertime Watermelon Energy Drink - 6pk/8 fl oz Cans' into search field
 #   When Click on search icon