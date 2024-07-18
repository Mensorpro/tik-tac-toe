class Player:
    id = 0
    def __init__(self, id, symbol):
        self.id = id
        self.symbol = symbol
        self.name = f"Player {id}"
        id += 1

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if not isinstance(other, Player):
            return False
        return self.id == other.id and self.symbol == other.symbol and self.name == other.name
    
    def __hash__(self):
        return hash((self.name, self.symbol))

    def __ne__(self, other):
        return not self.__eq__(other)