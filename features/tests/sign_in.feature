# Created by porter at 6/17/25
Feature: SignIn tests

  Scenario: 'Verify user can sign in'
    Given Open Target page
    When Click Sign In
    When Click Sign In from side nav menu
    Then Verify Sign in form opens


  Scenario: 'Verify error message displays when user enters an incorrect password'
    Given Open Target page
    When Click Sign In
    When Click Sign In from side nav menu
    When Enter valid email address
    When Click Create account with password
    When Enter incorrect password
    When Click Create account with password
    Then Verify error message displays