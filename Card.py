

class Card:
    suits = ("spade", "heart", "diamond", "club")
    rank = (6,7,8,9,10,11,12,13,14)

    def __init__(self, suit, rank):
        """ Initalizes a card
        suit: The suit of the card
        rank: The rank of the card
        """

        # Checks if card suit is valid
        if suit not in Card.suits:
            # Raises exception otherwise
            raise AttributeError("Must be valid suit")
        # Checks if card rank is valid
        if rank not in Card.rank:
            # Raises exception otherwise
            raise AttributeError("Must be valid rank")
        # Sets card attributes
        self.Suit = suit
        self.Rank = rank
