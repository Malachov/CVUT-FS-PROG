import itertools
import math
import random


class Game:
    def __init__(self, num_of_players):
        self.num_of_players = num_of_players
        self.moves_in_round = math.floor(32/num_of_players)
        self.deck = []
        self.players = []
        self.num_of_rounds = 0

    def create_deck_of_cards(self):
        """Creates a deck of cards (Currently as a list of Card objects)
        Input: None
        Output: None"""
        # make a deck of cards - tuples (DEPRICATED)
        # self.deck = list(itertools.product(range(7, 14), ['Srdce', 'Listy', 'Kule', 'Zaludy']))

        # make a deck of cards - instances of Card class
        colors = ["Srdce", "Listy", "Kule", "Zaludy"]
        values = list(range(7, 15))
        for color in colors:
            for value in values:
                self.deck.append(Card(color, value))

        # get rid of spare cards if there are 3 or 5 players
        if self.num_of_players != 4:
            # self.deck.remove((7, 'Zaludy')) # Deletes Zaludy 7 if self.deck is a list of tuples (DEPRICATED)
            # self.deck.remove((8, 'Zaludy')) # Deletes Zaludy 8 if self.deck is a list of tuples

            del self.deck[24]  # Deletes Zaludy 7
            del self.deck[25]  # Deletes Zaludy 8
        return self.deck

    def create_players(self):
        for i in range(self.num_of_players):
            player_name = input(f"Insert a name of the {i+1} player: ")
            self.players.append(Player(name=player_name, position=i))  # Individual players are stored in a list


class Round:
    def __init__(self):
        self.first_player = None
        self.isDoubled = False
        self.played_cards = []
        self.cards_to_player = None

    def choose_first_player(self, game):
        """Decides which player starts the next round
        Input: Game object
        Output: first_player_index (int)"""
        if game.num_of_rounds == 1:
            first_player_index = random.randint(0,game.num_of_players-1)
        else:
            pass  # Insert logic... the one who loses the last round should start the new one
        return first_player_index

    def deal_cards(self, game):
        random.shuffle(game.deck) # First of all, shuffle the deck of cards
        i = 0 # subsidiary variable for indexing in a for loop
        cards_for_one_player = math.floor(len(game.deck)/game.num_of_players)
        for player in game.players:
            player.cards_in_hand = game.deck[i*cards_for_one_player:(i+1)*cards_for_one_player]
            i += 1
    def display_played_cards_in_round(self, row = False, index = False):
        """Converts the Card objects into a readable form
        Input: None
        Output: string (formatted string)"""
        string = ""  # creates an empty string to which the cards will be written

        idx = 0
        for card in self.played_cards:
            if (row == False):
                string = string + f"\n({card.color}, {card.value})\n".upper()
            else: # we want to format the cards as a one column
                if index == False:
                    string = string + f"({card.color}, {card.value}) \n"
                else:
                    idx = idx + 1
                    string = string + f"({card.color}, {card.value});  {idx}. card\n"
        return string


class Player:
    def __init__(self, name, position, score=0, balance=0):
        self.name = name
        self.position = position
        self.score = score
        self.balance = balance
        self.cards_in_hand = []
        self.cards_on_table = []
        self.card_played = None

    def choose_card(self):
        """Select a card which is played by a player in a given round
        Input: None
        Output: card_played"""

        card_played_index = int(input(f"It is a {self.name}'s move. Choose one from the following cards of yours: \n"
              f"{self.display_cards_in_hand(row = True, index = True)}")) # choose the index of card to be played
        card_played = self.cards_in_hand[card_played_index-1] # choose the card which will be player;
                                                              # -1... offseting the indexing of cards
        return card_played

    def count_points(self):
        pass

    def display_cards_in_hand(self, row = False, index = False):
        '''Converts the Card objects into a readable form
        Input: None
        Output: string (formatted string)'''
        string = "" # creates an empty string to which the cards will be written

        idx = 0
        for card in self.cards_in_hand:
            if (row == False):
                string = string + f"({card.color}, {card.value})"
            else: # we want to format the cards as a one column
                if (index == False):
                    string = string + f"({card.color}, {card.value}) \n"
                else:
                    idx = idx + 1
                    string = string + f"({card.color}, {card.value});  {idx}. card\n"
        return string


class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value
