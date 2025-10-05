import pygame
from uiElements.baseUIElement import baseUIElement
from uiElements.TextObject import TextObject
from uiElements.button import Button

class DialogueWithChoice(baseUIElement):

    def __init__(self, x, y, buttonAssetUri=None, surface=None, questionText : TextObject = None, optionOneText : TextObject = None, optionTwoText : TextObject = None, optionThreeText : TextObject = None, optOneCallback: any = None, optTwoCallback: any = None, optThreeCallback: any = None):
        super().__init__(x, y, buttonAssetUri, surface, questionText)

