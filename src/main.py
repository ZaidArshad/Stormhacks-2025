# Example file showing a basic pygame "game loop"
import pygame
from scenes import titlescreen
from rendering.rendering import Renderer
from singletons.singletons import gameState, GameState, renderer, running

# pygame setup
running = True
pygame.init()
clock = pygame.time.Clock()
renderer = Renderer()
renderer.set_elements(titlescreen.PrepareGUIElements(renderer))

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
    pygame.display.update()

    clock.tick(60)  # limits FPS to 60

pygame.quit()