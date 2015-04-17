# CirclesGame.py - Updates and draws the game and the menu.
# Created by Josh Kennedy on 18 May 2014
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015 Sirkles LLC

import MainMenu

import ClassicMode
import LightningMode

class CirclesGame():
    def __init__(self):
        self.showMainMenu = True
        self.mainMenu = MainMenu.MainMenu()
        self.classicMode = ClassicMode.ClassicMode()
        self.gameplayMode = 0
        self.lightningMode = LightningMode.LightningMode()

    def update(self, deltaTime):
        if (self.gameplayMode is 1 and not self.classicMode.started and not self.classicMode.active):
            self.classicMode.startGame()

        if (self.gameplayMode is 2 and not self.lightningMode.started and not self.classicMode.active):
            self.lightningMode.startGame()

        if self.showMainMenu:
            self.mainMenu.update(deltaTime)

            self.showMainMenu = self.mainMenu.active
            self.gameplayMode = self.mainMenu.selectedGameMode
        else:
            if (self.gameplayMode is 1):
                # Classic mode.
                self.classicMode.update(deltaTime)
            if (self.gameplayMode is 2):
                # Lightning mode.
                self.lightningMode.update(deltaTime)

    def handleInput(self, event):
        if self.showMainMenu:
            self.mainMenu.handleInput(event)
        else:
            if (self.gameplayMode is 1):
                # Classic mode.
                self.classicMode.handleInput(event)
            if (self.gameplayMode is 2):
                # Lightning mode.
                self.lightningMode.handleInput(event)

    def draw(self, deltaTime):
        if self.showMainMenu:
            self.mainMenu.draw(deltaTime)
        else:
            if (self.gameplayMode is 1):
                # Classic mode.
                self.classicMode.draw(deltaTime)
            if (self.gameplayMode is 2):
                # Lightning mode.
                self.lightningMode.draw(deltaTime)
