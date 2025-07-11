# Created by porter at 6/2/25
Feature: Verify sign in for logged out users
  # verify a logged out user can navigate to Sign In

  Scenario: Logged out user can navigate to Sign In
    Given Open Target page
    When Click on Account
    And Click on sign in
    Then Open sign in form