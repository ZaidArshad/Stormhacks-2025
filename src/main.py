# Example file showing a basic pygame "game loop"
import pygame
import pygame_gui
from scenes import titlescreen
from rendering.rendering import Renderer
from singletons.singletons import screenX, screenY, gameState, uiManager, GameState, renderer

# pygame setup
pygame.init()
screen = pygame.display.set_mode((screenX, screenY))
clock = pygame.time.Clock()
uiManager = pygame_gui.UIManager((screenX, screenY)) 
renderer = Renderer()
running = True

renderer.set_elements(titlescreen.PrepareGUIElements())

while running:
    time_delta = clock.tick(60)/1000.0
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if gameState == GameState.TITLESCREEN:
        pass
        # titlescreen.Exec()
    elif gameState == GameState.GAME:
        pass
    elif gameState == GameState.ENDINGSCREEN:
        pass

    uiManager.draw_ui(renderer.get_screen())
    uiManager.update(time_delta)
    renderer.draw()
    pygame.display.update()

    clock.tick(60)  # limits FPS to 60

pygame.quit()