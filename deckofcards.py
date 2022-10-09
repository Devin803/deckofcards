class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return '{} of {}'.format(self.value, self.suit)

class Deck:

    def __init__(self):
        pass


class Player:

    def __init__(self,name):
        pass

card = Card("Hearts", 6)
print(card)