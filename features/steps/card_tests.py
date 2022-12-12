from behave import *
import deckofcards


@Given('I have created a new deck')
def step_impl(context):
    pass


@When('I create the new deck')
def step_impl(context):
    new_deck = deckofcards.Deck()


