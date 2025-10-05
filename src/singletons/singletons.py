from enum import Enum
from rendering.rendering import Renderer 

class GameState(Enum):
    TITLESCREEN = 1
    GAME = 2
    ENDINGSCREEN = 3

# game state
class Game():
    state = GameState.TITLESCREEN
    running = True

game = Game()

uiManager = None

renderer = Renderer()

uiEvtManager = None