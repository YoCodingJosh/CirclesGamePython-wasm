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
        self.textRender = TextEffects.Linefill_Text(self.text, AssetCache.gameOverFont, Colors.White.getTuple(), Colors.Gold.getTuple(), Colors.ForestGreen.getTuple())

    def update(self):
        pass

    def handleInput(self, event):
        pass

    def draw(self):
        # Since PyGame doesn't support alpha pixels in it's draw method, I have to directly blit a surface to the screen.
        pygame.display.get_surface().blit(self.background, (0, 0))

        # Render and draw the text.
        renderSurface = self.textRender.render()
        renderSurface.set_colorkey(Colors.White.getTuple())
        pygame.display.get_surface().blit(renderSurface, (0, 0))


    def restartGame(self):
        pass

    def gotoMenu(self):
        pass
