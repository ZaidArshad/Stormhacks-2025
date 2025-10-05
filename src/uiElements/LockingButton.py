from uiElements.button import Button
from singletons.singletons import game, renderer, uiEvtManager

class LockingButton(Button):
    def __init__(self, x, y, buttonAssetUri=None, surface=None, buttonHoverAssetUri = "", TextObject = None):
        super().__init__(x, y, buttonAssetUri, surface, buttonHoverAssetUri, self.execCallback, TextObject)
        # when created it should lock interface
        game.dialogue_lock = True
        uiEvtManager.setLocking(self)
        renderer.add_element(self)

    def execCallback(self):
        game.dialogue_lock = False
        uiEvtManager.clearLocking()
        renderer.remove_element(self)