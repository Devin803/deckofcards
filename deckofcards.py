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

    def create_deck(self):
        for cards in ["Hearts", "Clubs", "Diamonds", "Spades"]:
            for numbers in range(1, 14):
                self.cards.append(Card(cards, numbers))


class Player:

    def __init__(self, name):
        pass

create = Deck()
print(create)