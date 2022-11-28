Feature: Testing all deck of cards classes
  Scenario: test that you can create a deck of cards
    Given I have created a new deck
    When I create the new class
    Then There should be an empty list of cards

  Scenario: creating a deck gives me 52 cards
    Given I create a deck of cards
    When I create a new class
    Then I have 52 cards in the deck with appropriate suits

  Scenario: Test that cards will get shuffled
    Given I have a deck of cards
    When I shuffle the cards
    Then The order will be randomized

