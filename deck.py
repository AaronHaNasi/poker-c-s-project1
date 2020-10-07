import random

class deck:
    def __init__():
        cards = ['AC', '2C'. '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC',
        'QC', 'KC', 'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH',
        'QH', 'KH', 'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD',
        'QD', 'KD', 'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS',
        'QS', 'KS']
        # Cards are defined as follows 1-10, J = Jack, Q = Queen, K = King, A = Ace.
        # Second character defines suite. C = Clubs, H = Hearts, D = Diamonds, and
        # S = Spades

    # Returns a random card from the deck. Only pulls from cards that haven't
    # been pulled yet.
    def deal:
        random.shuffle(deck)
        return deck.pop()

    def reset:
        cards = ['AC', '2C'. '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC',
        'QC', 'KC', 'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH',
        'QH', 'KH', 'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD',
        'QD', 'KD', 'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS',
        'QS', 'KS']
        return
