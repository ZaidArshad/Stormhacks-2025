# Example file showing a basic pygame "game loop"
import pygame
import pygame_gui
from scenes import titlescreen
from singletons.singletons import screenX, screenY, gameState, uiManager, GameState, renderer

# pygame setup
pygame.init()
screen = pygame.display.set_mode((screenX, screenY))
clock = pygame.time.Clock()
running = True
uiManager = pygame_gui.UIManager((screenX, screenY)) 

titlescreen.Draw()

while running:
    time_delta = clock.tick(60)/1000.0
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if gameState == GameState.TITLESCREEN:
        titlescreen.Exec()
    elif gameState == GameState.GAME:
        pass
    elif gameState == GameState.ENDINGSCREEN:
        pass

    renderer.draw()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()