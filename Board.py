import math
import Player
import Library
import random


# Board Class, Everything will be built on top of this.
class Board:
    def __init__(self, num_of_players=4, passed=True, winner_starts=True):
        """
        Initializes board.
        num_of_players: number of players that will play the game
        passed: whether you can pass cards in the game
        """
        # Checks if enough players are in the game
        if num_of_players < 2:
            # Raises error otherwise
            raise AttributeError("Can't Play with less than 2 people")
        # Calculates and keeps the number of players that are playing and the number of decks it needs to shuffle
        self.Num_of_players = num_of_players
        self.Num_of_decks = math.floor(num_of_players/5)
        # Creates Deck Object
        self.Current_Library = Library.Library(self.Num_of_decks)
        # Creates list of players
        self.Players = [Player.Player() for x in range(self.Num_of_players)]
        # Sets game type
        self.Passed = passed
        # Sets if the winner starts next game
        self.Winner_starts = winner_starts
        # Initializes all the unknown variables
        self.trump_suit = None
        self.current_turn = 0
        self.attack_zone = None
        self.mode = None
        self.winner = None

    def start_game(self):
        """
        Stars game
        """
        # Shuffles Library
        self.Current_Library.shuffle_library()
        # Deals out 6 cards
        for x in range(6):
            # To each player
            for player in self.Players:
                player.add_card(self.Current_Library.get_next_card())
        # Sets the trump suit, as the bottom card.
        self.trump_suit = self.Current_Library.bottom_card().Suit
        # Randomly chooses starting player
        self.current_turn = random.randint(0, self.Num_of_players-1)
        # Sets game to attacking phase
        self.mode = "A"

    def get_available_moves(self, player_index):
        if self.mode == "A":
            return ()





