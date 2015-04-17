# LightningMode.py - Sorta like classic, but different background and thunder and lightning.
# Created by Josh Kennedy on 13 July 2014
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015 Sirkles LLC

import pygame

import AssetCache
import Colors
import HighScore

class LightningMode():
    def __init__(self):
        self.score = -1
        self.highScoreObject = HighScore.HighScore()
        self.highScore = self.highScoreObject.getScore("Lightning")
        self.started = False
        self.active = False

    def startGame(self):
        #Lights! Camera! ACTION!!
        self.score = 0
        self.started = True
        self.active = True;
        print("wow")

    def update(self, deltaTime):
        if not self.active: return
        pass

    def handleInput(self, event):
        if not self.active: return
        pass

    def draw(self, deltaTime):
        if not self.active: return

        pygame.display.get_surface().fill(Colors.Black.getTuple())

        scoreSurface = AssetCache.scoreFont.render("Score: " + str(self.score), True, Colors.White.getTuple())

        pygame.display.get_surface().blit(scoreSurface, (0, 0))

        placeholderSurface = AssetCache.buttonFont.render("I have no idea what to put here. Any ideas?", True, Colors.Gold.getTuple())

        renderX = pygame.display.get_surface().get_width() / 2 - placeholderSurface.get_rect().centerx
        renderY = pygame.display.get_surface().get_height() / 2 - placeholderSurface.get_rect().centery

        pygame.display.get_surface().blit(placeholderSurface, (renderX, renderY))
