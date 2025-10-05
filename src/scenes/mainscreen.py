import pygame
import pygame_gui
import pathlib
from rendering.rendering import Renderer
from uiElements.button import Button
from uiElements.baseUIElement import baseUIElement
from singletons.singletons import running

laptop = None
book = None
redbull = None

def PrepareGUIElements(renderer: Renderer):
    ''''''
    global laptop, book, redbull
    relpath = pathlib.Path( "assets" ) / "placeholder" 
    bg_rect = renderer.get_background().get_rect()
    laptop = Button(bg_rect.left+100, bg_rect.centery-350, 
                    buttonAssetUri= relpath / "main_laptop_base.png",
                    buttonHoverAssetUri= relpath / "main_laptop_hover.png")
    book = Button(bg_rect.centerx-300, bg_rect.bottom-300, 
                  buttonAssetUri= relpath / "main_book_base.png",
                  buttonHoverAssetUri= relpath / "main_book_hover.png")
    redbull = Button(bg_rect.centerx+700, bg_rect.centery-100, 
                     buttonAssetUri= relpath / "main_redbull_base.png",
                     buttonHoverAssetUri= relpath / "main_redbull_hover.png")
    # menu interaction btns

    return [laptop, book, redbull]


def Init():
    ''''''

def Exec():
    ''''''
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()

        mouse_pos = pygame.mouse.get_pos()
        laptop.check_hovered(mouse_pos)
        book.check_hovered(mouse_pos)
        redbull.check_hovered(mouse_pos)
