

Feature: Cart tests

  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open Target page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown


  Scenario: Add a product to cart
    Given Open Target page
    When Click Target product A-92785491 page
    When Click the add to cart button
    When Click 'View cart & check out' button
    Then Verify product is in cart