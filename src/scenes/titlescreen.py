import pygame
import pygame_gui
from singletons.singletons import screenX, screenY, uiManager

startGame = None
closeGame = None

def PrepareGUIElements():
    ''''''
    global startGame, closeGame
    original_image = pygame.image.load('assets\placeholder\startScreen_bg.png').convert()
    background_image = pygame.transform.scale(original_image, (screenX,screenY))

    # menu interaction btns
    startBtnRect = pygame.Rect((350, 275), (100, 50)) # (x, y), (width, height)
    quitBtnRect = pygame.Rect((650, 275), (100, 50))
    startGame = pygame_gui.elements.UIButton(relative_rect=startBtnRect, text='Play', manager=uiManager)   
    closeGame = pygame_gui.elements.UIButton(relative_rect=quitBtnRect, text='Quit', manager=uiManager)   

    return [background_image]


def Init():
    ''''''

def Exec():
    ''''''
    for event in pygame.event.get():
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == startGame:
                pass
        uiManager.process_events(event)