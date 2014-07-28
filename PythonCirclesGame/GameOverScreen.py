# GameOverScreen.py - Displays the user's scores and the option to retry or quit.
# Created by Josh Kennedy on 23 July 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

import pygame

import AssetCache
import Colors
import HighScore

class GameOverScreen():
    def __init__(self, gameplayMode, userScore):
        self.gameplayMode = gameplayMode
        self.userScore = userScore

    def update(self):
        pass

    def handleInput(self, event):
        pass

    def draw(self):
        pass

    def restartGame(self):
        pass

    def gotoMenu(self):
        pass
