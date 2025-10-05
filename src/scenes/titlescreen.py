import pygame
import pygame_gui
from rendering.rendering import Renderer
from uiElements.button import Button
from uiElements.baseUIElement import baseUIElement
from singletons.singletons import running

startGame = None
closeGame = None

def PrepareGUIElements(renderer: Renderer):
    ''''''
    global startGame, closeGame
    screen_size = renderer.get_screen_size()
    original_image = pygame.image.load('assets/placeholder/startScreen_bg.png').convert()
    background_image =  baseUIElement(0,0, surface= pygame.transform.scale(original_image, screen_size))
    start_button = Button(500, 450, buttonAssetUri= "assets\\ui\\default\\startGame.png")
    quit_button = Button(500, 650, buttonAssetUri= "assets\\ui\\hover\\startGameHover.png")
    # menu interaction btns


    return [background_image, start_button, quit_button]


def Init():
    ''''''

def Exec():
    ''''''
    global running
    for event in pygame.event.get():
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            pass
