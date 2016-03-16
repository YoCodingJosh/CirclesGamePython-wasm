# GameOverScreen.py - Displays the user's scores and the option to retry or quit.
# Created by Josh Kennedy on 23 July 2014
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015-2016 Sirkles LLC

import pygame

import random

import AssetCache
import Colors
import HighScore
import Rectangle
import TextEffects
import HelperAPI

class GameOverScreen():
    """The screen that is displayed to the user after they lose."""

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
            self.text = "Congratulations! You have a new high score!"

        # Render the message text.
        self.messageSurface = TextEffects.textDropShadow(AssetCache.gameOverFont, self.text, 5, Colors.Red.getTuple(), Colors.DarkMediumGray.getTuple())
        #self.messageSurface.set_colorkey(Colors.Black.getTuple())
        self.messageXPosition = HelperAPI.getCenterOfScreen()[0] - self.messageSurface.get_width() / 2
        self.messageYPosition = HelperAPI.getCenterOfScreen()[1] - self.messageSurface.get_height() / 2
        self.messageYPositionLowerLimit = self.messageYPosition - 163

        # Render the score text.
        scoreText = "Your Score: " + str(userScore) + "       " + "High Score: " + str(highScore)
        self.scoreSurface = TextEffects.textDropShadow(AssetCache.scoreFont, scoreText, 2, Colors.DarkOrange.getTuple(), Colors.Black.getTuple())
        self.scoreXPosition = HelperAPI.getCenterOfScreen()[0] - self.scoreSurface.get_width() / 2
        self.scoreYPosition = HelperAPI.getCenterOfScreen()[1] - self.scoreSurface.get_height() / 2
        self.scoreYPosition -= 50

        # Set up animations.
        self.transitionDone = False
        self.waitingTime = 80
        self.waiting = True

    def update(self, deltaTime):
        if self.transitionDone: return

        # We wait for roughly a second before we start the animations.
        if (self.waitingTime > 0):
            self.waitingTime -= 1
        elif (self.waitingTime <= 0):
            self.waiting = False

        if (not self.waiting and not self.transitionDone):
            if (self.messageYPosition > self.messageYPositionLowerLimit):
                self.messageYPosition -= int((3 * deltaTime) * 100)
            else:
                self.transitionDone = True

    def handleInput(self, event):
        pass

    def draw(self):
        # Since PyGame doesn't support alpha pixels in it's draw method, I have to directly blit a surface to the screen.
        pygame.display.get_surface().blit(self.background, (0, 0))

        # Draw the text at the center of the screen.
        pygame.display.get_surface().blit(self.messageSurface, (self.messageXPosition, self.messageYPosition))

        if self.transitionDone:
            pygame.display.get_surface().blit(self.scoreSurface, (self.scoreXPosition, self.scoreYPosition))

    def restartGame(self):
        pass

    def gotoMenu(self):
        pass
