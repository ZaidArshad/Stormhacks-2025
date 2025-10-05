from singletons.singletons import game, GameState

class Player:
    def __init__(self):
        self.sanity = 100

    def lower_sanity(self, delta):
        self.sanity -= delta
        if (self.sanity <= 0):
            game.state = GameState.ENDINGSCREEN

    
    