from random import shuffle
from numpy import append

class Card(object):
    """Representation of the card
    
    Parameters
    ---------------------
    rank: integer
        The number which reffers to the rank of the card as shown:
            2 - 2
            3 - 3
            4 - 4
            5 - 5
            6 - 6
            7 - 7
            8 - 8
            9 - 9
            10 - 10
            11 - Jack
            12 - Queen
            13 - King
            14 - Ace
    suit: integer
        The number which refferes to the suit of the card as shown:
            0 - Hearts
            1 - Diamonds
            2 - Clubs
            3 - Spades
    """
    def __init__(self, rank, suit):
            self.rank = rank
            self.suit = suit

class Deck(object):
    """Representation of the deck of cards

    Attributes
    ----------
    cards: list
        Current cards in the deck
    """
    def __init__(self):
        self.cards = []
        for i in range(4):
            for j in range(2,15):
                temp_obj = Card(rank=j, suit=i)
                self.cards.append(temp_obj)

    def shuffleDeck(self):
        """Shuffling the deck of cards"""
        return shuffle(self.cards)

    def pickTopCard(self):
        """Picking a card from the top of the deck"""
        return self.cards.pop(0)

    def burnCard(self):
        """Burning the card"""
        self.cards.append(self.pickTopCard())