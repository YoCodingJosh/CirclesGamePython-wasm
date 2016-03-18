# CreditsMenu.py - The credits for Pop a Dots.
# Created by Josh Kennedy on 16 March 2016
#
# Pop a Dots
# Copyright 2015-2016 Sirkles LLC

import pygame

import AssetCache

import Circle
import CircleButton
import Colors
import HelperAPI
import TextEffects

class CreditsMenu():
    """Credits of Pop a Dots."""

    def __init__(self, mainMenu):
        self.title = TextEffects.textWavey(AssetCache.titleFont, "Pop a Dots", Colors.White.getTuple(), 5)
        self.titleSurface = self.title.animate()
        self.mainMenuInstance = mainMenu

    def update(self, deltaTime):
        self.titleSurface = self.title.animate(deltaTime)

    def handleInput(self, event):
        pass

    def draw(self):
        pygame.display.get_surface().blit(self.titleSurface, (HelperAPI.getWindowRectangleAsRectangle().width - self.titleSurface.get_width() - 100, 300))
