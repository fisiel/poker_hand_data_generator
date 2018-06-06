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

    def isRoyalFlush(self, hand):
        """Chcecking if the hand is royal flush
        
        Parameters
        ----------
        hand: list
            Combination of five different cards
        """
        if not all(hand[0].color == card.color for card in hand):
            return False
        else:
            for card in hand:
                try:
                    if not next(hand).figure - card.figure > 1:
                        return False
                except StopIteration:
                    pass
            if hand[0].figure == 10:
                return True
            else:
                return False

    def isStraightFlush(self, hand):
        """Chcecking if the hand is royal flush
        
        Parameters
        ----------
        hand: list
            Combination of five different cards
        """
        if not all(hand[0].color == card.color for card in hand):
            return False
        else:
            for card in hand:
                try:
                    if not next(hand).figure - card.figure > 1:
                        return False
                except StopIteration:
                    pass                
            return True
    
    def isFourOfAKind(self, hand):
        """Chcecking if the hand is four of a kind
        
        Parameters
        ----------
        hand: list
            Combination of five different cards
        """
        check_sum = 0
        for reference in hand:
            for card in hand:
                if reference.figure == card.figure:            
                    check_sum +=1
            if check_sum == 4:
                return True
        return False

    def isFullHouse(self, hand):
        """Chcecking if the hand is full house
        
        Parameters
        ----------
        hand: list
            Combination of five different cards
        """
        check_sum = [0, 0, 0]
        temp_hand = hand
        for reference in temp_hand:
            for card in temp_hand:
                if reference.figure == card.figure:            
                    check_sum[0] +=1
            if check_sum[0] == 3:
                temp_hand.pop(temp_hand.index(reference))
                check_sum[1] += 1
            elif check_sum[0] == 2:
                temp_hand.pop(temp_hand.index(reference))
                check_sum[2] += 1
            check_sum[0] = 0 
        if (check_sum[1] and check_sum[2]) == 1:
            return True
        else:          
            return False

    def isFlush(self, hand):
        """Chcecking if the hand is flush
        
        Parameters
        ----------
        hand: list
            Combination of five different cards
        """
        if not all(hand[0].color == card.color for card in hand):
            return False
        else:
            return True

    def isStraight(self, hand):
        """Chcecking if the hand is straight
        
        Parameters
        ----------
        hand: list
            Combination of five different cards
        """
        for card in hand:
            try:
                if not next(hand).figure - card.figure > 1:
                    return False
            except StopIteration:
                pass               
        return True

    def isThreeOfAKind(self, hand):
        """Chcecking if the hand is three of a kind
        
        Parameters
        ----------
        hand: list
            Combination of five different cards
        """
        check_sum = 0
        for reference in hand:
            for card in hand:
                if reference.figure == card.figure:            
                    check_sum +=1
            if check_sum == 3:
                return True
            check_sum = 0
        return False
    
    def isTwoPairs(self, hand):
        """Chcecking if the hand is two pairs
        
        Parameters
        ----------
        hand: list
            Combination of five different cards
        """
        check_sum = [0, 0]
        temp_hand = hand
        for reference in temp_hand:
            for card in temp_hand:
                if reference.figure == card.figure:            
                    check_sum[0] +=1
            if check_sum[0] == 2:
                temp_hand.pop(temp_hand.index(reference))
                check_sum[1] += 1
                if check_sum[1] == 2:
                    return True
            check_sum[0] = 0
        return False

    def isOnePair(self, hand):
        """Chcecking if the hand is one pair
        
        Parameters
        ----------
        hand: list
            Combination of five different cards
        """
        check_sum = 0
        for reference in hand:
            for card in hand:
                if reference.figure == card.figure:            
                    check_sum +=1
            if check_sum == 2:
                return True
            check_sum = 0
        return False

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
        if self.isRoyalFlush(hand):
            return 9
        elif self.isStraightFlush(hand):
            return 8
        elif self.isFourOfAKind(hand):
            return 7
        elif self.isFullHouse(hand):
            return 6
        elif self.isFlush(hand):
            return 5
        elif self.isStraight(hand):
            return 4
        elif self.isThreeOfAKind(hand):
            return 3
        elif self.isTwoPairs(hand):
            return 2
        elif self.isOnePair(hand):
            return 1
        else:
            return 0
