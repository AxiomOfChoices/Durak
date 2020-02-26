

class Player:
    def __init__(self):
        """Initializes Player with empty hand
        """
        # Sets the initial hand to be empty
        self.hand = []
        # Sets the hand size to be 0
        self.hand_size = 0

    def add_card(self, card):
        """Adds card to player hand
        card: Card object that will be added
        """
        # Adds a card to the card list
        self.hand.append(card)
        # Increments size
        self.hand_size += 1

    def play_cards(self, indexes):
        """Removes cards from the player hand
        indexes: List of indexes of the cards to be removed, all must be less than the hand size and bigger or equal to \
        0
        """
        # Creates a new array with all the cards played
        cards_played = [self.hand[i] for i in range(self.hand_size-1) if i in indexes]
        # Sets the new hand to be the hand minus all the cards played
        self.hand = [self.hand[i] for i in range(self.hand_size-1) if i not in indexes]
        # Returns the played cards
        return cards_played
