# PlayGameMenu.py - Where the player can select a game mode.
# Created by Josh Kennedy on 31 May 2014
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015-2016 Sirkles LLC

import pygame

import AssetCache

import Colors
import Circle
import CircleButton

class PlayGameMenu():
    """Lets the player decide which game mode to play and then transfers control to that game mode."""

    def __init__(self, mainMenu):
        self.classicModeCircleButton = CircleButton.CircleButton(700, 150, 100, Colors.White, Colors.SteelBlue, AssetCache.buttonFont)
        self.classicModeCircleButton.text = "Classic"
        self.classicModeCircleButton.clickEvent = self.startClassicMode

        self.classicBackgroundCircle = Circle.Circle(700, 150, 100)

        self.lightningModeCircleButton = CircleButton.CircleButton(950, 150, 100, Colors.Purple, Colors.LawnGreen, AssetCache.buttonFont)
        self.lightningModeCircleButton.text = "Lightning"
        self.lightningModeCircleButton.clickEvent = self.startLightningMode

        self.lightningBackgroundCircle = Circle.Circle(950, 150, 100)

        self.mainMenuInstance = mainMenu

        self.active = True

    def update(self, deltaTime):
        if not self.active: return

        self.classicModeCircleButton.update(deltaTime) 
        self.lightningModeCircleButton.update(deltaTime)

        # Transition from Play Game Menu to Classic Mode
        if (self.mainMenuInstance.selectedGameMode is 1 and self.mainMenuInstance.transitionToMenu and self.classicBackgroundCircle.radius <= 1220):
            self.classicBackgroundCircle.radius += int((6 * deltaTime) * 100)
        elif (self.mainMenuInstance.selectedGameMode is 1 and self.classicBackgroundCircle.radius >= 1220):
            self.active = False
            self.mainMenuInstance.active = False

        # Transition from Play Game Menu to Lightning Mode
        if (self.mainMenuInstance.selectedGameMode is 2 and self.mainMenuInstance.transitionToMenu and self.lightningBackgroundCircle.radius <= 1220):
            self.lightningBackgroundCircle.radius += int((6 * deltaTime) * 100)
        elif (self.mainMenuInstance.selectedGameMode is 2 and self.lightningBackgroundCircle.radius >= 1220):
            self.active = False
            self.mainMenuInstance.active = False

    def handleInput(self, event):
        if not self.active: return

        self.classicModeCircleButton.handleInput(event)
        self.lightningModeCircleButton.handleInput(event)

    def draw(self, deltaTime):
        if not self.active: return

        self.classicModeCircleButton.draw(Colors.DarkOrange, Colors.DeepPink)

        self.lightningModeCircleButton.draw(Colors.Black, Colors.White)

        if (self.mainMenuInstance.selectedGameMode == 1):
            self.classicBackgroundCircle.draw(Colors.White)
        elif (self.mainMenuInstance.selectedGameMode == 2):
            self.lightningBackgroundCircle.draw(Colors.Black)

    def startClassicMode(self):
        AssetCache.highPop2Sound.play()
        self.mainMenuInstance.selectedMenu = -1
        self.mainMenuInstance.transitionToMenu = True
        self.mainMenuInstance.selectedGameMode = 1
        self.mainMenuInstance.backCircleButton.clickable = False
        self.classicModeCircleButton.active = False
        self.lightningModeCircleButton.clickable = False

    def startLightningMode(self):
        AssetCache.highPopSound.play()
        self.mainMenuInstance.selectedMenu = -1
        self.mainMenuInstance.transitionToMenu = True
        self.mainMenuInstance.selectedGameMode = 2
        self.mainMenuInstance.backCircleButton.clickable = False
        self.classicModeCircleButton.clickable = False
        self.lightningModeCircleButton.active = False
