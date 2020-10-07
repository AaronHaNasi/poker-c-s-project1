class player:# Player object
    def __init__(self, name):
    self.name = name
    hand = []
    tokens = 100
    is_small_blind = False
    is_big_blind = False
    folded = False
