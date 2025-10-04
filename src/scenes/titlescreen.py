import pygame
from singletons.singletons import screenX, screenY

screen = pygame.display.set_mode((screenX, screenY))
def init():
    ''''''
    original_image = pygame.image.load('assets\placeholder\startScreen_bg.png').convert()

    # Scale the image to match the screen size exactly
    background_image = pygame.transform.scale(original_image, (screenX,screenY))
    screen.blit(background_image, (0, 0))

