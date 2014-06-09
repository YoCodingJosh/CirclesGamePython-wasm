# PlayGameMenu.py - Where the player can select a game mode.
# Created by Josh Kennedy on 31 May 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

import pygame

import AssetCache

import Colors
import Circle
import CircleButton

import ClassicMode

class PlayGameMenu():
    def __init__(self, mainMenu):
        self.classicModeCircleButton = CircleButton.CircleButton(700, 150, 100, Colors.Khaki, Colors.SteelBlue, AssetCache.buttonFont)
        self.classicModeCircleButton.text = "Classic"
        self.classicModeCircleButton.clickEvent = self.startClassicMode

        self.classicBackgroundCircle = Circle.Circle(700, 150, 100)

        self.mainMenuInstance = mainMenu

        self.active = True

    def update(self, deltaTime):
        if not self.active: return

        if (self.mainMenuInstance.selectedGameMode == 1 and self.mainMenuInstance.transitionToMenu and self.classicBackgroundCircle.radius <= 1220):
            self.classicBackgroundCircle.radius += int((6 * deltaTime) * 100)
        elif (self.mainMenuInstance.selectedGameMode == 1 and self.mainMenuInstance.transitionToMenu and self.classicBackgroundCircle.radius >= 1220):
            self.active = False
            self.mainMenuInstance.active = False
            del self.mainMenuInstance
            del self

    def handleInput(self, event):
        if not self.active: return

        self.classicModeCircleButton.handleInput(event)

    def draw(self, deltaTime):
        if not self.active: return

        self.classicModeCircleButton.draw(Colors.White, Colors.LawnGreen)

        if (self.mainMenuInstance.selectedGameMode == 1):
            self.classicBackgroundCircle.draw(Colors.White)

    def startClassicMode(self):
        AssetCache.highPop2Sound.play()
        self.mainMenuInstance.selectedMenu = -1
        self.mainMenuInstance.transitionToMenu = True
        self.mainMenuInstance.selectedGameMode = 1
        self.mainMenuInstance.backCircleButton.clickable = False
