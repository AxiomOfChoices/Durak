

class Player:
    def __init__(self):
        """Initializes Player with empty hand
        """
        self.hand = []
        self.hand_size = 0

    def add_card(self, card):
        """Adds card to player hand
        card: Card object that will be added
        """
        self.hand.append(card)
        self.hand_size += 1

    def play_cards(self, indexes):
        """Removes cards from the player hand
        indexes: List of indexes of the cards to be removed, all must be less than the hand size and bigger than 0
        """
        cards_played = [self.hand[i] for i in range(self.hand_size-1) if i in indexes]
        self.hand = [self.hand[i] for i in range(self.hand_size-1) if i not in indexes]
        return cards_played
