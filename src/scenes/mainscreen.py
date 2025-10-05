import pygame
import pygame_gui
import pathlib
from rendering.rendering import Renderer
from uiElements.button import Button
from uiElements.baseUIElement import baseUIElement
from singletons.singletons import running

startGame = None
closeGame = None

def PrepareGUIElements(renderer: Renderer):
    ''''''
    relpath = pathlib.Path( "assets" ) / "placeholder" 
    laptop = Button(200, 200, buttonAssetUri= relpath / "main_laptop_base.png")
    book = Button(300, 300, buttonAssetUri= relpath / "main_book_base.png")
    redbull = Button(400, 400, buttonAssetUri= relpath / "main_redbull_base.png")
    # menu interaction btns

    return [laptop, book, redbull]


def Init():
    ''''''

def Exec():
    ''''''
    global running
    for event in pygame.event.get():
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            pass
