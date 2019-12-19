

class Player:
    def __init__(self):
        """
        Initializes Player with empty hand
        """
        self.hand = []
        self.hand_size = 0

    def add_card(self, card):
        """
        Adds card to player hand
        card: Card object that will be added
        """
        self.hand.append(card)
        self.hand_size += 1

    def play_card(self, index):
        """
        Removes the card from the player hand
        index: Index of the card to be removed, must be less than the hand size and bigger than 0
        """
        card_played = self.hand.pop(index)
        return card_played
