import pygame
from rendering.rendering import Renderer
from uiElements.uiEvtManager import UiEventManager
from uiElements.button import Button
from uiElements.baseUIElement import baseUIElement
from singletons.singletons import game, GameState, renderer, uiEvtManager
from pathlib import Path
from scenes import mainscreen
startGame = None
closeGame = None

def PrepareGUIElements(renderer: Renderer, uiEvtManager: UiEventManager):
    ''''''
    global startGame, closeGame
    screen_size = renderer.get_screen_size()
    original_image = pygame.image.load(Path('assets/placeholder/startScreen_bg.png')).convert()
    background_image =  baseUIElement(0,0, surface= pygame.transform.scale(original_image, screen_size))

    original_image = pygame.image.load(Path('assets/placeholder/startScreen_btn_play.png')).convert()
    x_pos = screen_size[0]//2 - original_image.width//2
    y_pos = screen_size[1]//2 - original_image.height//2
    start_button = Button(x_pos, y_pos, buttonAssetUri= Path("assets/placeholder/startScreen_btn_play.png"), callback=startGame)
    quit_button = Button(x_pos, y_pos+200, buttonAssetUri= Path("assets/placeholder/startScreen_btn_quit.png"), callback=shutdownGame)
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
    print("closing game")
    game.state = False
    exit()

def startGame():
    print("starting game")
    game.state = GameState.GAME
    renderer.set_elements(mainscreen.PrepareGUIElements(renderer))

