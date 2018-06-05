from random import shuffle
from numpy import append

class Card(object):
    """Representation of the card
    
    Parameters
    ---------------------
    figure: integer
        The number which reffers to the figure of the card as shown:
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
    color: integer
        The number which refferes to the color of the card as shown:
            0 - Hearts
            1 - Diamonds
            2 - Clubs
            3 - Spades
    """
    def __init__(self, figure, color):
            self.figure = figure
            self.color = color

class Deck(object):
    """Representation of the deck of cards
    
    Parameters
    ----------
    None

    Attributes
    ----------
    cards: list
        Current cards in the deck
    """
    def __init__(self):
        self.cards = []
        for i in range(4):
            for j in range(2,15):
                temp_obj = Card(figure=j, color=i)
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

class Player(object):
    """Representation of the poker game player
    
    Parameters
    ----------
    name: string
        Name of the player
    cash: integer
        Value of the player cash
    data_input: Unknown
        Decision from outside of script

    Attributes
    ----------
    cash_round: integer
        Player's cash in the bidding round
    current_bid: integer
        Current bid of the player
    hole_cards: list
        Two cards in player's hand
    game: PokerGame object
        Game which is being joined by the player
    position: integer
        Current player position at the table
    decision: integer
        The number which reffers to the players decision as shown:
            0 - fold
            1 - check
            2 - bid
            3 - call

    competitor_decisions: matrix
        Other players' decisions formatted:
            [[player1, player1, player2, player2,...],
             [decision_p1, bid_p1, decision_p2, bid_p2...],
             ...]
    """
    def __init__(self, name, cash, data_input):
        self.name = name
        self.cash = cash
        self.data_input = data_input
        self.cash_round = 0
        self.current_bid = 0
        self.hole_cards = []
        self.decision = 0
        self.competitors_decisions = []
        
d = "rdctfvygbuhnubvyfcdttgbuhvfcfdtxsrtdfhgftrhftrfctfcg"+
"fdgfgvhgbjnkubgftryvgubhnijbvyfyvgubhnijm"

    def joinGame(self, game):
        """Adding the player to the game"""   
        self.game = game     
        self.game.players.append(self)
        self.cash = self.game.standard_cash

    def getPosition(self):
        """Retrieving current position of the player at the table"""
        self.position = self.game.players.index(self)

    def receiveCard(self, card):
        """Retrieving the card dealt by the dealer
        
        Parameters
        ----------
        card: Card object
            Card dealt to the player by the dealer
        """
        self.hole_cards.append(card)

    def bid(self):
        """Bidding by the player"""
        self.decision = self.data_input[0]
        self.current_bid = self.data_input[1]
        self.cash -= self.current_bid
        self.cash_round += self.current_bid

    def initializeObservation(self):
        """Initializing data collection, adding other players' names"""
        for player in self.game.players:
            if player.name != self.name:
                for i in range(2):
                    self.competitors_decisions.append(player.name)
        self.competitors_decisions = [self.competitors_decisions]

    def observePlayers(self):
        """Collect data about other players' decisions"""
        temp = []
        for player in self.game.players:
            if player.name != self.name:
                temp.append(player.decision)
                temp.append(player.current_bid)
        temp = [temp]
        append(self.competitors_decisions, temp, 0)

class Dealer(object):
    """Representation of the dealer

    Parameters
    ----------
    game: PokerGame object
        The game witch the dealer joins
    """
    def __init__(self, game):
        self.game = game

    def dealCards(self):
        """Dealing cards""" 
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
        """Showing one hidden community card to all players"""
        self.game.visible_community_cards += 1

class PokerGame(object):
    """Representation of the poker round

    Parameters
    ----------
    None

    Attributes
    ----------
    players: list
        All players in the game
    dealer: Dealer object
        Dealer in the game
    community_cards: list
        Cards on the table
    visible_community_cards: integer
        Number of visible community cards
    bank: list
        Amount of cash in the round
    deck: Deck object
        The deck of card used in the game
    forced_bids: list
        Predefined small bid and big bid
    standard_cash: integer
        Standard amount of money player starts game with
    """
    def __init__(self):
        self.players = []
        self.dealer = None 
        self.community_cards = []
        self.visible_community_cards = 0
        self.bank = []
        self.deck = Deck()
        self.forced_bids = [10, 20]
        self.standard_cash = 500

    def moveDealerButton(self):
        """Shitft players list so that a different player is the dealer"""
        self.players.append(self.players.pop(0))

    def startGame(self):
        """Create dealer instance and deal cards"""
        self.dealer = Dealer(self)
        self.dealer.dealCards()

    def checkBidMatch(self):
        """Check if all players' bids are qual
        
        Returns
        -------
        1 - all bids are equal
        0 - bids are not equal
        """
        for nom_player in self.players:
            for player in self.players:
                if player.cash_round != nom_player.cash_round:
                    return 0
        return 1            

    def biddingRound(self):
        """Plyers are bidding until all bids are equal"""
        while not self.checkBidMatch():
            for player in self.players:
                if self.players.index(player) == 0:
                    player_dealer = player
                elif self.players.index(player) == (len(self.players) - 1):
                    player.bid()
                    player_dealer.bid()
