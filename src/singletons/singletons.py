from enum import Enum
# screen size
screenX = 1920
screenY = 1080

# game state
class GameState(Enum):
    TITLESCREEN = 1
    GAME = 2
    ENDINGSCREEN = 3

gameState = GameState.TITLESCREEN

uiManager = None

renderer = None