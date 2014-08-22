# GameOverScreen.py - Displays the user's scores and the option to retry or quit.
# Created by Josh Kennedy on 23 July 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

import pygame

import random

import AssetCache
import Colors
import HighScore
import Rectangle
import TextEffects
import HelperAPI

class GameOverScreen():
    def __init__(self, gameplayMode, userScore, highScore):
        self.gameplayMode = gameplayMode
        self.userScore = userScore
        self.highScore = highScore

        # Save time and pre-render the background and text surfaces.
        self.background = pygame.Surface(AssetCache.screenResolution, pygame.SRCALPHA) # Create surface with per-pixel alpha.
        self.background.fill(Colors.TransparentWhite.getTuple()) # Fill with the transparent white color.

        # Figure out what to say.
        if (userScore < highScore):
            self.text = "You didn't break your high score."
        elif (userScore == highScore):
            self.text = "You've tied your high score. So close!"
        else:
            self.text = "You have a new high score!! Congratulations!"

        # Render the text.
        self.renderSurface = TextEffects.textDropShadow(AssetCache.gameOverFont, self.text, 5, Colors.Red.getTuple(), Colors.DarkMediumGray.getTuple())
        self.renderSurface.set_colorkey(Colors.Black.getTuple())

    def update(self):
        # Animations!! :D
        pass

    def handleInput(self, event):
        pass

    def draw(self):
        # Since PyGame doesn't support alpha pixels in it's draw method, I have to directly blit a surface to the screen.
        pygame.display.get_surface().blit(self.background, (0, 0))

        # Render and draw the text.
        pygame.display.get_surface().blit(self.renderSurface, (HelperAPI.getCenterOfScreen()[0] - self.renderSurface.get_width() / 2, HelperAPI.getCenterOfScreen()[1] - self.renderSurface.get_height() / 2))

    def restartGame(self):
        pass

    def gotoMenu(self):
        pass
