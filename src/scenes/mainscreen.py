import pygame
import pathlib
from singletons.singletons import game, renderer
from rendering.rendering import Renderer
from uiElements.uiEvtManager import UiEventManager
from uiElements.button import Button
from uiElements.baseUIElement import baseUIElement
from player.player import Player

laptop = None
book = None
redbull = None
player = None

def laptopClick():
    print("laptop click")
    if game.input_delay > 1:
        if game.laptop_interaction in [0,2,3,5,6]:
            renderer.toggle_laptop_view()
        if game.laptop_interaction not in [0,2,3,5,6]:
            game.laptop_interaction += 1
            renderer.set_laptop_view_num(game.laptop_interaction)
        game.input_delay = 0

def bookClick():
    print("book click")
    if game.input_delay > 1:
        renderer.toggle_notebook_view()
        game.input_delay = 0

def redbullClick():
    print("redbull click")
    if game.input_delay > 1:
        player.drink_redbull()
        game.input_delay = 0

def PrepareGUIElements(renderer: Renderer, uiEvtManager: UiEventManager):
    ''''''

    global laptop, book, redbull, player
    relpath = pathlib.Path( "assets" ) / "placeholder" 
    bg_rect = renderer.get_background().get_rect()
    laptop = Button(bg_rect.left+100, bg_rect.centery-350, 
                    buttonAssetUri= relpath / "main_laptop_base.png",
                    buttonHoverAssetUri= relpath / "main_laptop_hover.png", callback=laptopClick)
    book = Button(bg_rect.centerx-300, bg_rect.bottom-300, 
                  buttonAssetUri= relpath / "main_book_base.png",
                  buttonHoverAssetUri= relpath / "main_book_hover.png", callback=bookClick)
    redbull = Button(bg_rect.right-500, bg_rect.centery-100, 
                     buttonAssetUri= relpath / "main_redbull_base.png",
                     buttonHoverAssetUri= relpath / "main_redbull_hover.png", callback=redbullClick)
    
    uiEvtManager.register(laptop)
    uiEvtManager.register(book)
    uiEvtManager.register(redbull)
    
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
            if event.key == pygame.K_ESCAPE and not renderer.get_is_laptop_view():
                game.running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if renderer.get_is_laptop_view():
                laptopClick()

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
            player.lower_sanity(1)
