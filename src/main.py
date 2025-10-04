# Example file showing a basic pygame "game loop"
import pygame
from scenes import titlescreen
from singletons.singletons import screenX, screenY, gameState, GameState

# pygame setup
pygame.init()
screen = pygame.display.set_mode((screenX, screenY))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RENDER YOUR GAME HERE
    if gameState == GameState.TITLESCREEN:
        titlescreen.init()
    elif gameState == GameState.GAME:
        pass
    elif gameState == GameState.ENDINGSCREEN:
        pass

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()