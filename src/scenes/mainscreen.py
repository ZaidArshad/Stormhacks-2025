import pygame
import pathlib
from singletons.singletons import game, renderer
from rendering.rendering import Renderer
from uiElements.button import Button
from uiElements.baseUIElement import baseUIElement
from player.player import Player

laptop = None
book = None
redbull = None
player = None

def PrepareGUIElements(renderer: Renderer):
    ''''''
    global laptop, book, redbull, player
    relpath = pathlib.Path( "assets" ) / "placeholder" 
    bg_rect = renderer.get_background().get_rect()
    laptop = Button(bg_rect.left+100, bg_rect.centery-350, 
                    buttonAssetUri= relpath / "main_laptop_base.png",
                    buttonHoverAssetUri= relpath / "main_laptop_hover.png")
    book = Button(bg_rect.centerx-300, bg_rect.bottom-300, 
                  buttonAssetUri= relpath / "main_book_base.png",
                  buttonHoverAssetUri= relpath / "main_book_hover.png")
    redbull = Button(bg_rect.right-500, bg_rect.centery-100, 
                     buttonAssetUri= relpath / "main_redbull_base.png",
                     buttonHoverAssetUri= relpath / "main_redbull_hover.png")
    
    player = Player()
    # menu interaction btns

    return [laptop, book, redbull]


def Init():
    ''''''

def Exec(events : list[pygame.event.Event]):
    ''''''
    for event in events:
        if event.type == pygame.QUIT:
             game.running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game.running = False

        mouse_pos = pygame.mouse.get_pos()
        renderer.set_camera_offset(*mouse_pos)

        if laptop:
            laptop.check_hovered(mouse_pos)
        if book:
            book.check_hovered(mouse_pos)
        if redbull:
            redbull.check_hovered(mouse_pos)

        if player:
            pass
            # player.lower_sanity(1)
