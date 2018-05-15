"""
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

0 - Hearts
1 - Diamonds
2 - Clubs 
3 - Spades
"""
import random

class Card(object):
        def __init__(self, figure, color):
            self.figure = figure
            self.color = color

class Deck(object):
    def __init__(self):
        card_number = 0
        self.cards = []

        for i in range(4):
            for j in range(2,15):
                temp_obj = Card(figure=0, color=0)
                self.cards.append(temp_obj)
                self.cards[card_number].color = i
                self.cards[card_number].figure = j
                card_number += 1

    def shuffleDeck(self):
        return random.shuffle(self.cards)

    def pickTopCard(self):
        return self.cards.pop(0)
    
    def burnCard(self):
        temp_card = self.cards.pop(0)
        self.cards.append(temp_card)

class Player(object):
    def __init__(self, name, cash, *args):
        self.name = name
        self.cash = cash
        self.game = args[0]
        self.current_bid = 0
        self.hand = [] #dopisać funkcję oceniającą aktualne karty w ręce
        self.position = 0
        
    def receiveCard(self, card):
        self.hand.append(card)

    def bid(self, bid):
        self.current_bid = bid
    
    def forcedBid(self):
        if self.position == 1:
            self.bid(self.game.forcedBid[self.position])
        elif self.position == 2:
            self.bid(self.game.forcedBid[self.position])

    def changePosition(self, position):
        self.position = position

class Dealer(object):
    def __init__(self, game):
        self.game = game
        
    def dealCards(self):
        self.game.deck.shuffleDeck()

        for i in range(2):
            for player_number in range(self.game.players):
                self.game.players[player_number].receiveCard(self.game.deck.pickTopCard())

        self.game.deck.burnCard()

        for i in range(3):
            self.game.community_cards.append(self.game.deck.pickTopCard())
        
        for i in range(2):
            self.game.deck.burnCard()

            self.game.community_cards.append(self.game.deck.pickTopCard())

    def unfoldCommunityCard(self):
        temp_card = self.game.community_cards.pop(0)
        for player_number in range(len(self.game.players)):
            self.game.players[player_number].hand.append(temp_card)

class pokerGame(object):
    def __init__(self):
        self.players = []
        self.dealer = Dealer(self)
        self.community_cards = []
        self.bank = 0
        self.deck = Deck()
        self.forcedBids = []