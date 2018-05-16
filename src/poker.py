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
        self.cards = []

        for i in range(4):
            for j in range(2,15):
                temp_obj = Card(figure=j, color=i)
                self.cards.append(temp_obj)

    def shuffleDeck(self):
        return random.shuffle(self.cards)

    def pickTopCard(self):
        return self.cards.pop(0)

    def burnCard(self):
        temp_card = self.cards.pop(0)
        self.cards.append(temp_card)

class Player(object):
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.current_bid = 0
        self.hole_cards = []
        self.position = 0

    def joinGame(self, game):   
        self.game = game     
        self.position = self.game.players.index(self)

    def receiveCard(self, card):
        self.hole_cards.append(card)

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
        self.game.visible_community_cards += 1

class PokerGame(object):
    def __init__(self):
        self.players = []
        self.dealer = None #self.dealer = Dealer(self) dodać później
        self.community_cards = []
        self.visible_community_cards = 0
        self.bank = 0
        self.deck = Deck()
        self.forcedBids = [10, 20]
        self.standard_cash = 500
    
    def addPlayer(self, player):
       self.players.append(player)
    
    def moveDealerButton(self):
        self.players.append(self.players.pop(0))
  
game = PokerGame()
game.addPlayer(Player("Janusz", game.standard_cash))
game.addPlayer(Player("Lol", game.standard_cash))
game.addPlayer(Player("Pirat", game.standard_cash))
game.addPlayer(Player("Dzwonek", game.standard_cash))
game.players[0].joinGame(game)
game.players[1].joinGame(game)
game.players[2].joinGame(game)
game.players[3].joinGame(game)
game.moveDealerButton()
