from singletons.singletons import game, GameState, renderer
import pygame
from pathlib import Path
from uiElements.baseUIElement import baseUIElement 
from uiElements.dialogueWithChoices import DialogueWithChoice
from uiElements.TextObject import TextObject
from uiElements.LockingButton import LockingButton


class Player:
    def __init__(self):
        self.sanity = 100
        self.hallucination = [False] * 6

    def lower_sanity(self, delta):
        self.sanity -= delta
        bg_rect = renderer.get_background().get_rect()

        if self.sanity <= 85 and not self.hallucination[1]:
            self.hallucination[1] = True
            book_dropping_sound = pygame.mixer.Sound(Path("assets/sound_effects/bookDropping.wav"))
            book_dropping_sound.play()
        if self.sanity <= 75 and not self.hallucination[2]:
            self.hallucination[2] = True
            blood = baseUIElement(bg_rect.centerx-100, bg_rect.centery+100, surface= pygame.image.load(Path('assets/final/final_san75_overlay.png')).convert_alpha())
            renderer.add_element(blood)
        if self.sanity <= 60 and not self.hallucination[3]:
            self.hallucination[3] = True
            shadow = baseUIElement(bg_rect.centerx-200, bg_rect.top-140, surface= pygame.image.load(Path('assets/final/final_san60_overlay.png')).convert_alpha())
            renderer.add_element(shadow)
        if self.sanity <= 50 and not self.hallucination[4]:
            self.hallucination[4] = True
            bloody_bull = baseUIElement(bg_rect.centerx+554, bg_rect.centery+11, surface= pygame.image.load(Path('assets/final/final_san50_overlay.png')).convert_alpha())
            renderer.add_element(bloody_bull)
        if self.sanity <= 35 and not self.hallucination[5]:
            self.hallucination[5] = True
            laptop_flash = baseUIElement(bg_rect.centerx-815, bg_rect.centery-270, surface= pygame.image.load(Path('assets/final/final_san35_overlay.png')).convert_alpha())
            renderer.add_element(laptop_flash)
            red_aura = baseUIElement(0, 0, surface= pygame.image.load(Path('assets/final/final_large_overlay.png')).convert_alpha())
            renderer.add_element(red_aura)
        if self.sanity <= 0:
            game.state = GameState.ENDINGSCREEN
        print(self.sanity)

    def drink_redbull(self):
        redbull_sound = pygame.mixer.Sound(Path("assets/sound_effects/drinkRedbull.wav"))
        if game.redbull_interaction < 3:
            redbull_sound.play()
        bg_rect = renderer.get_background().get_rect()
        if game.redbull_interaction == 0:
            LockingButton(300, bg_rect.centery + 100, Path("assets/UI/dialog_bubble_regular.png"), TextObject= TextObject("I feel a bit more awake", Path("assets/Tox Typewriter.ttf"), 30, (255, 255, 255), (150, 150)))
        if game.redbull_interaction == 1:
            LockingButton(300, bg_rect.centery + 100, Path("assets/UI/dialog_bubble_regular.png"), TextObject= TextObject("This is helping... just a little. But I'm a bit shaky.", Path("assets/Tox Typewriter.ttf"), 30, (255, 255, 255), (150, 150)))
            self.lower_sanity(5)
        if game.redbull_interaction == 2:
            LockingButton(300, bg_rect.centery + 100, Path("assets/UI/dialog_bubble_regular.png"), TextObject= TextObject("That was my last sip.", Path("assets/Tox Typewriter.ttf"), 30, (255, 255, 255), (150, 150)))
            self.lower_sanity(10)
        game.redbull_interaction += 1
        print(game.redbull_interaction)
    
    def do_homework(self):
        bg_rect = renderer.get_background().get_rect()
        if game.notebook_interaction == 0:
            LockingButton(300, bg_rect.centery + 100, Path("assets/UI/dialog_bubble_regular.png"), TextObject= TextObject("my brain just won't process anything now. Everything's noise...", Path("assets/Tox Typewriter.ttf"), 30, (255, 255, 255), (150, 150)))
        if game.notebook_interaction == 1:    
            pass
        if game.notebook_interaction == 2: 
            pass
        game.notebook_interaction += 1
        print(game.notebook_interaction)        