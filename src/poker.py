import random

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
        return random.shuffle(self.cards)

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

    Attributes
    ----------
    current_bid: integer
        Current bid of the player
    hole_cards: list
        Two cards in player's hand
    position: integer
        Current player position at the table
    game: PokerGame object
        Game which is being joined by the player
    """
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.current_bid = 0
        self.hole_cards = []
        self.position = 0

    def joinGame(self, game):
        """Adding the player to the game"""   
        self.game = game     
        self.game.players.append(self)
    
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

    def bid(self, bid):
        """Bidding by the player
        """
        self.current_bid += bid

    def forcedBid(self):
        """Bidding the forced bids by the player if obliged"""
        if self.position == 1:
            self.bid(self.game.forcedBid[self.position])
        elif self.position == 2:
            self.bid(self.game.forcedBid[self.position])

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
    forcedBid: list
        Predefined small bid and big bid
    standard_cash: integer
        Standard amount of money player starts game with
    """
    def __init__(self):
        self.players = []
        self.dealer = None #self.dealer = Dealer(self) dodać później
        self.community_cards = []
        self.visible_community_cards = 0
        self.bank = []
        self.deck = Deck()
        self.forcedBids = [10, 20]
        self.standard_cash = 500

    def moveDealerButton(self):
        """Shitft players list so that different player is the dealer"""
        self.players.append(self.players.pop(0))
