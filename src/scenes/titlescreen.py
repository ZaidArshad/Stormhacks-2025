import pygame
from rendering.rendering import Renderer
from uiElements.uiEvtManager import UiEventManager
from uiElements.button import Button
from uiElements.baseUIElement import baseUIElement
from singletons.singletons import running
from pathlib import Path
startGame = None
closeGame = None

def PrepareGUIElements(renderer: Renderer, uiEvtManager: UiEventManager):
    ''''''
    global startGame, closeGame
    screen_size = renderer.get_screen_size()
    original_image = pygame.image.load(Path('assets/placeholder/startScreen_bg.png')).convert()
    background_image =  baseUIElement(0,0, surface= pygame.transform.scale(original_image, screen_size))

    start_button = Button(500, 450, buttonAssetUri= Path("assets/placeholder/startScreen_btn_play.png"), callback=startGame)
    quit_button = Button(500, 650, buttonAssetUri= Path("assets/placeholder/startScreen_btn_quit.png"), callback=shutdownGame)
    uiEvtManager.register(start_button)
    uiEvtManager.register(quit_button)

    return [background_image, start_button, quit_button]


def Init():
    ''''''

def Exec():
    ''''''
    # global running
    # for event in pygame.event.get():
    #     if event.type == pygame_gui.UI_BUTTON_PRESSED:
    pass

# helper functions
def shutdownGame():
    global running
    print("closing game")
    running = False
    pygame.quit()

def startGame():
    print("starting game")

