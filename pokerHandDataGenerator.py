from pokerClasses import Card, Deck
import csv

class PokerHandDataGenerator(object):
    """Poker hand data generator

    Attributes
    ----------
    deck: Deck object
        The deck of cards used to generate hands
    """
    def __init__(self):
        self.deck = Deck()

    def classifyHand(self, hand):
        """Classifing poker hands
        
        Parameters
        ----------
        hand: list
            Combination of five different cards
        
        Returns
        -------
        hand_rank: integer
            Rank of the hand:
                0 - no pair
                1 - one pair
                2 - two pairs
                3 - three of a kind
                4 - straight
                5 - flush
                6 - full house
                7 - four of a kind
                8 - straight flush
                9 - royal flush
        """
        sorted(hand, key=lambda card: card.figure)
        iterator = iter(hand)
        
    
    def isRoyalFlush(self, iterator):
        """Chcecking if the hand is royal flush
        
        Parameters
        ----------
        hand: list
            Combination of five different cards
        """
        first = next(iterator)
        check_color = all(first.color == card.color for card in iterator)
        check_figure = all((first.figure - card.figure) > 1 for card in iterator)
        if check_color and check_figure and first.figure == 10:
            return True
        else:
            return False
        

    def isStraightFlush(self, iterator):
        """Chcecking if the hand is straight flush
        
        Parameters
        ----------
        hand: list
            Combination of five different cards
        """
        first = next(iterator)
        check_color = all(first.color == card.color for card in iterator)
        check_figure = all((first.figure - card.figure) > 1 for card in iterator)
        if check_color and check_figure:
            return True
        else:
            return False

    def isFlush(self, iterator):
        """Chcecking if the hand is flush
        
        Parameters
        ----------
        hand: list
            Combination of five different cards
        """
        first = next(iterator)
        check_color = all(first.color == card.color for card in iterator)
        if check_color:
            return True
        else:
            return False

    def isStraight(self, iterator):
        """Chcecking if the hand is straight
        
        Parameters
        ----------
        hand: list
            Combination of five different cards
        """
        first = next(iterator)
        check_figure = all((first.figure - card.figure) > 1 for card in iterator)
        if check_figure:
            return True
        else:
            return False
        

            
