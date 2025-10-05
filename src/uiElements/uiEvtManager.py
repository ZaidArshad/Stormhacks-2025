from button import Button
import pygame
class uiEventManager:

    def __init__(self):
        self.activeUIElements: list[Button]= []

    def clear(self):
        self.activeUIElements.clear()

    def process(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("hiii")
                # for uielement in self.activeUIElements:
