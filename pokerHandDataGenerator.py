from pokerClasses import Card, Deck

class PokerHandDataGenerator(object):
    """Poker hand data generator"""

    def isRoyalFlush(self, hand):
        """Chcecking if the hand is royal flush
        
        Parameters
        ----------
        hand: list
            Combination of five different cards

        Returns
        -------
        True or False
        """
        if self.isStraightFlush(hand) and hand[0].rank == 10:
            return True
        else:
            return False

    def isStraightFlush(self, hand):
        """Chcecking if the hand is straight flush
        
        Parameters
        ----------
        hand: list
            Combination of five different cards

        Returns
        -------
        True or False
        """
        if self.isFlush(hand) and self.isStraight(hand):
            return True
        else:
            return False
    
    def isFourOfAKind(self, hand):
        """Chcecking if the hand is four of a kind
        
        Parameters
        ----------
        hand: list
            Combination of five different cards

        Returns
        -------
        True or False
        """
        check_sum = 0
        for reference in hand:
            for card in hand:
                if reference.rank == card.rank:            
                    check_sum +=1
            if check_sum == 4:
                return True
            check_sum = 0
        return False

    def isFullHouse(self, hand):
        """Chcecking if the hand is full house
        
        Parameters
        ----------
        hand: list
            Combination of five different cards

        Returns
        -------
        True or False
        """
        check_sum = [0, 0]
        temp_hand = list(hand)
        for reference in temp_hand:
            for card in temp_hand:
                if reference.rank == card.rank:            
                    check_sum[0] +=1
            if check_sum[0] == 3:
                temp_hand.pop(temp_hand.index(reference))
                check_sum[1] += 1
                break
            check_sum[0] = 0
        temp_hand = list(hand)
        for reference in temp_hand:
            for card in temp_hand:
                if reference.rank == card.rank:            
                    check_sum[0] +=1
            if check_sum[0] == 2:
                temp_hand.pop(temp_hand.index(reference))
                check_sum[1] += 1
                break
            check_sum[0] = 0
        if check_sum[1] == 2:
            return True
        else:
            return False

    def isFlush(self, hand):
        """Chcecking if the hand is flush
        
        Parameters
        ----------
        hand: list
            Combination of five different cards

        Returns
        -------
        True or False
        """
        for i in range(0, len(hand)-1):
            if hand[i+1].suit != hand[i].suit:
                return False
        return True

    def isStraight(self, hand):
        """Chcecking if the hand is straight
        
        Parameters
        ----------
        hand: list
            Combination of five different cards

        Returns
        -------
        True or False
        """
        for i in range(0, len(hand)-1):
            if (hand[i+1].rank - hand[i].rank) != 1:
                return False
        return True

    def isThreeOfAKind(self, hand):
        """Chcecking if the hand is three of a kind
        
        Parameters
        ----------
        hand: list
            Combination of five different cards

        Returns
        -------
        True or False
        """
        check_sum = 0
        for reference in hand:
            for card in hand:
                if reference.rank == card.rank:            
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

        Returns
        -------
        True or False
        """
        check_sum = [0, 0]
        temp_hand = list(hand)
        for reference in temp_hand:
            for card in temp_hand:
                if reference.rank == card.rank:            
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

        Returns
        -------
        True or False
        """
        for reference in hand:
            temp_hand = list(hand)
            temp_hand.pop(hand.index(reference))
            for card in temp_hand:
                if card.rank == reference.rank:           
                    return True
            temp_hand.append(reference)
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
        sorted(hand, key=lambda card: card.rank)
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
    
    def createDataRow(self, hand):
        """Creates list of integers from original data

        Parameters
        ----------
        hand: list
            Combination of five different cards
        
        Returns
        -------
        formatted_list: list
            List of integers obtainded from objects 
        """
        formatted_list = []
        for card in hand:
            formatted_list.append(card.suit)
            formatted_list.append(card.rank)
        formatted_list.append(self.classifyHand(hand))
        return formatted_list
    
    def generatePokerHands(self):
        """Generates every possible poker hand
        
        Returns
        -------
        num: integer
            Number of hand instances
        """
        deck_1 = Deck()
        for card_1 in deck_1.cards:
            deck_2 = deck_1
            deck_2.cards.pop(deck_1.cards.index(card_1))
            filename = 'poker_hand_%s_%s.data' % (card_1.suit, card_1.rank)
            file = open(filename, 'a+')
            for card_2 in deck_2.cards:
                deck_3 = deck_2
                deck_3.cards.pop(deck_2.cards.index(card_2))
                for card_3 in deck_3.cards:
                    deck_4 = deck_3
                    deck_4.cards.pop(deck_3.cards.index(card_3))
                    for card_4 in deck_4.cards:
                        deck_5 = deck_4
                        deck_5.cards.pop(deck_4.cards.index(card_4))
                        for card_5 in deck_5.cards:
                            hand = self.createDataRow([card_1, card_2, card_3, card_4, card_5])
                            hand = str(hand).strip('[]')
                            file.write(hand + "\n")
                        deck_5.cards.append(card_4)
                    deck_4.cards.append(card_3)
                deck_3.cards.append(card_2)
            deck_2.cards.append(card_1) 
            file.close()      
    
data_generator = PokerHandDataGenerator()
data_generator.generatePokerHands()