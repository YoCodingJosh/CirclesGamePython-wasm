# CreditsMenu.py - The credits for Pop a Dots.
# Created by Josh Kennedy on 16 March 2016
#
# Pop a Dots
# Copyright 2015-2016 Sirkles LLC

import pygame

import AssetCache

import Colors
import HelperAPI
import TextEffects

import PythonCirclesGame


class CreditsMenu:
    """Credits of Pop a Dots."""

    def __init__(self, main_menu):
        self.title = TextEffects.TextWavey(AssetCache.titleFont, "Pop a Dots", Colors.White.get_tuple(), 5)
        self.titleSurface = self.title.animate()
        self.mainMenuInstance = main_menu
        self.versionText = AssetCache.buttonFont.render("Version " + PythonCirclesGame.__version__, True,
                                                        Colors.Gold.get_tuple())

    def update(self, delta_time):
        self.titleSurface = self.title.animate(delta_time)

    def handleInput(self, event):
        pass

    def draw(self):
        pygame.display.get_surface().blit(self.titleSurface, (HelperAPI.getWindowRectangleAsRectangle().width -
                                                              self.titleSurface.get_width() - 222, 50))
        pygame.display.get_surface().blit(self.versionText, (HelperAPI.getWindowRectangleAsRectangle().width -
                                                             self.titleSurface.get_width() - 222,
                                                             self.titleSurface.get_height() + 75))
