import random


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return '{} of {}'.format(self.value, self.suit)


class Deck:

    def __init__(self):
        # Create an empty list for cards
        self.cards = []
        self.create_deck()

    def create_deck(self):
        for suits in ["Hearts", "Clubs", "Diamonds", "Spades"]:
            for numbers in range(1, 14):
                self.cards.append(Card(suits, numbers))

    def shuffle_deck(self):
        for i in range(len(self.cards) - 1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]


class Player:

    def __init__(self, name):
        self.name = name



deck = Deck()
print(deck)