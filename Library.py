import Card
import random

class Library:
    def __init__(self, number_of_decks):
        """ Initializes a library made up of multiple decks
        number_of_decks: Number of decks to shuffle to get the library
        """
        # initializes list of cards
        self.cards = []
        # loops through the number of decks
        for deck in range(number_of_decks):
            # for each suit
            for suit in Card.Card.suits:
                # for each rank
                for rank in Card.Card.ranks:
                    # add a card with that suit and rank
                    self.cards.append(Card.Card(suit, rank))

    def get_next_card(self):
        """Returns next card and removes it from the top of the library
        """
        if len(self.cards) == 0:  # If there are no more cards left
            return None  # Return nothing
        else:  # If there are
            return self.cards.pop(len(self.cards)-1)  # Remove and return the last card

    def bottom_card(self):
        """Returns, without removing, the bottom card of the library
        """
        if len(self.cards) == 0:  # If there are no more cards left
            return None  # Return nothing
        else:  # If there are
            return self.cards[0]  # Return the bottom card

    def shuffle_library(self):
        """Shuffles library
        """
        random.shuffle(self.cards)  # Shuffle the deck


