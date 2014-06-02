# PlayGameMenu.py - Where the player can select a game mode.
# Created by Josh Kennedy on 31 May 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

import pygame

import AssetCache

import Colors
import CircleButton

class PlayGameMenu():
    def __init__(self):
        self.classicModeCircleButton = CircleButton.CircleButton(700, 150, 100, Colors.Khaki, Colors.SteelBlue, AssetCache.buttonFont)
        self.classicModeCircleButton.text = "Classic"
        self.classicModeCircleButton.clickEvent = self.startClassicMode

    def update(self, deltaTime):
        self.classicModeCircleButton.update(deltaTime)

    def handleInput(self, event):
        self.classicModeCircleButton.handleInput(event)

    def draw(self, deltaTime):
        self.classicModeCircleButton.draw(Colors.White, Colors.LawnGreen)

    def startClassicMode(self):
        print("wow")
