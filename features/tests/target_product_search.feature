Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Target page
    When Input 'Pencil' into search field
    When Click on search icon
    Then Product results for 'Pencil' are shown

  Scenario: Verify number of benefit cells
    Given Open Target page
    When Open Target Circle page
    Then Verify Circle page has '10' or more cells

  Scenario: User can add a product to the cart
    Given Open Target page
    When Input 'V8 +Energy Summertime Watermelon Energy Drink - 6pk/8 fl oz Cans' into search field
    When Click on search icon
    When Click the add to cart button
    When Choose options and add to cart
    When Click view cart
    Then Verify 'V8 +Energy Summertime Watermelon Energy Drink - 6pk/8 fl oz Cans' is in the cart