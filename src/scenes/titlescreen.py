import pygame
import pygame_gui
from singletons.singletons import screenX, screenY, uiManager

screen = pygame.display.set_mode((screenX, screenY))

startGame = None
closeGame = None

def Draw():
    ''''''
    global startGame, closeGame
    original_image = pygame.image.load('assets\placeholder\startScreen_bg.png').convert()
    background_image = pygame.transform.scale(original_image, (screenX,screenY))
    screen.blit(background_image, (0, 0))

    # menu interaction btns
    startBtnRect = pygame.Rect((350, 275), (100, 50)) # (x, y), (width, height)
    quitBtnRect = pygame.Rect((650, 275), (100, 50))
    startGame = pygame_gui.elements.UIButton(relative_rect=startBtnRect, text='Play', manager=uiManager)   
    closeGame = pygame_gui.elements.UIButton(relative_rect=quitBtnRect, text='Quit', manager=uiManager)   


def Init():
    ''''''

def Exec():
    ''''''
    for event in pygame.event.get():
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == startGame:
                print("helloooo")
        uiManager.process_events(event)