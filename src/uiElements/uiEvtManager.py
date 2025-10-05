from uiElements.button import Button
import pygame
class UiEventManager:

    def __init__(self):
        self.activeUIElements: list[Button]= []

    def register(self, button):
        self.activeUIElements.append(button)

    def clear(self):
        self.activeUIElements.clear()

    def process(self, events: list[pygame.event.Event]):
        for event in events:
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for uielement in self.activeUIElements:
                    if uielement.is_clicked(pos): 
                        uielement.execCallback()
            for uielement in self.activeUIElements:          
                uielement.check_hovered(pos)